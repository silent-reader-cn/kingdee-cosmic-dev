# 千户集团名册信息表-tcvvt_clique_mcinfo

## 千户集团名册信息表-主表 t_tcvvt_clique_mcinfo

- **表名称：** 千户集团名册信息表-主表
- **表名：** t_tcvvt_clique_mcinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 30 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 3 | fsynyysr | 上一年度营业收入（单位：万元） | numeric | 23 | 10 | √ | 0 | 上一年度营业收入（单位：万元） |
| 4 | fleverno | 企业管理层级编号 | varchar | 50 |  | √ | ' ' | 企业管理层级编号 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fregistertypeid | 登记注册类型 | int8 | 64 |  | √ | 0 | [注册登记类型 tax_info_registertype](../tctb_files/tax_info_registertype.md) |
| 7 | fcreditcode | 统一社会信用代码 | varchar | 50 |  | √ | ' ' | 统一社会信用代码 |
| 8 | fstockno | 股票代码 | varchar | 50 |  | √ | ' ' | 股票代码 |
| 9 | flocaltaxsn | 纳税人识别号（地税） | varchar | 50 |  | √ | ' ' | 纳税人识别号（地税） |
| 10 | fsuperorgname | 上级企业名称 | varchar | 100 |  | √ | ' ' | 上级企业名称 |
| 11 | flocaltaxorg | 地税局主管税务机关 | varchar | 50 |  | √ | ' ' | 地税局主管税务机关 |
| 12 | fnationtaxorg | 国税局主管税务机关 | varchar | 50 |  | √ | ' ' | 国税局主管税务机关 |
| 13 | felectronicfileno | 电子档案号 | varchar | 50 |  | √ | ' ' | 电子档案号 |
| 14 | fadress | 所在国家/地区 | varchar | 100 |  | √ | ' ' | 所在国家/地区 |
| 15 | fisvirtualnode | 是否为虚拟结点 | varchar | 30 |  | √ | ' ' | 是否为虚拟结点,枚举: 1 :是 2 :否 |
| 16 | fispointcompany | 是否为重点税源企业 | varchar | 30 |  | √ | ' ' | 是否为重点税源企业,枚举: 1 :是 2 :否 |
| 17 | fsynjnse | 上一年度缴纳税额（单位：万元） | numeric | 23 | 10 | √ | 0 | 上一年度缴纳税额（单位：万元） |
| 18 | ftaxername | 纳税人名称 | varchar | 50 |  | √ | ' ' | 纳税人名称 |
| 19 | fcommiterphone | 填表人联系电话 | varchar | 50 |  | √ | ' ' | 填表人联系电话 |
| 20 | fewblname | 二维表行名称 | varchar | 100 |  | √ | ' ' | 二维表行名称 |
| 21 | fnationtaxsn | 纳税人识别号（国税） | varchar | 50 |  | √ | ' ' | 纳税人识别号（国税） |
| 22 | fcommitername | 填表人姓名 | varchar | 50 |  | √ | ' ' | 填表人姓名 |
| 23 | fispubliccompany | 是否为上市公司 | varchar | 30 |  | √ | ' ' | 是否为上市公司,枚举: 1 :是 2 :否 |
| 24 | faccountway | 核算方式 | varchar | 50 |  | √ | ' ' | 核算方式 |
| 25 | fcodeandnameid | 国标行业（主行业） | int8 | 64 |  | √ | 0 | 行业代码及名称 tpo_tcvat_industrycode |
| 26 | fsbbid | 申报表id | varchar | 100 |  | √ | ' ' | 申报表id |
| 27 | fgrouproll | 集团名称 | varchar | 100 |  | √ | ' ' | 集团名称 |
| 28 | fisabroad | 是否为境外企业 | varchar | 30 |  | √ | ' ' | 是否为境外企业,枚举: 1 :是 2 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_clique_mcinfo2 |  | fsbbid |
| 2 | idx_tcvvt_clique_mcinfo |  | fewblxh,fsbbid |
| 3 | pk_tcvvt_clique_mcinfo |  | fid |
