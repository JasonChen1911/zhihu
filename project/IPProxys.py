#coding=utf-8
#ip 代理池 爬取免费ip构成代理池 供爬虫使用
import databases
import ip_proxys_manage as ipm

def gethosts():
    database = databases.Database('zhihu_info')
    database.connectdb()
    sql = 'SELECT * FROM ip_proxys WHERE status = 1 ORDER BY RAND() LIMIT 10;' 
    database.executedb(sql)
    hosts = []
    host_infos = database.value
    if host_infos:
        for item in host_infos:
            id = item[0]
            protocol = item[1]
            ip = item[2]
            port = item[3]
            status = item[4]
            if ipm.is_validity(protocol, ip, port): 
                hosts.append({protocol : protocol + "://" + ip + ":" + port})
            else:
                sql = "UPDATE ip_proxys SET status = 0 WHERE id = %s;" %(id)
                database.executedb(sql)
    else:
        print("提取ip失败...")        

    database.closedb()

    if hosts:
        return hosts
    else:
        gethosts()

def main():
    hosts = gethosts()
    print(hosts)

if __name__ == '__main__':
    main()