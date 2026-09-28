# 名册信息-tcvvt_roll_list

## 名册信息-主表 t_tcvvt_group_org

- **表名称：** 名册信息-主表
- **表名：** t_tcvvt_group_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 集团方案 | int8 | 64 |  | √ | 0 | [集团名册 tcvvt_group_book](../tcvvt_files/tcvvt_group_book.md) |
| 2 | forgcode | forgcode | varchar | 50 |  | √ | ' ' |  |
| 3 | fleverno | 企业管理层级编号 | varchar | 50 |  | √ | ' ' | 企业管理层级编号 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fregistertypeid | 登记注册类型 | int8 | 64 |  | √ | 0 | [注册登记类型 tax_info_registertype](../tctb_files/tax_info_registertype.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreditcode | 统一社会信用代码 | varchar | 50 |  | √ | ' ' | 统一社会信用代码 |
| 9 | fstockno | 股票代码 | varchar | 50 |  | √ | ' ' | 股票代码 |
| 10 | fenddate | 有效期止 | timestamp | 0 |  |  | null | 有效期止 |
| 11 | flocaltaxsn | 纳税人识别号（地税） | varchar | 50 |  | √ | ' ' | 纳税人识别号（地税） |
| 12 | fsuperorgname | 上级企业名称 | varchar | 100 |  | √ | ' ' | 上级企业名称 |
| 13 | ftrade | ftrade | varchar | 50 |  | √ | ' ' |  |
| 14 | flocaltaxorg | 地税局主管税务机关 | varchar | 50 |  | √ | ' ' | 地税局主管税务机关 |
| 15 | fnationtaxorg | 国税局主管税务机关 | varchar | 50 |  | √ | ' ' | 国税局主管税务机关 |
| 16 | fremark | fremark | varchar | 200 |  | √ | ' ' |  |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fparentid | 父组织id | int8 | 64 |  | √ | 0 | 父组织id |
| 19 | felectronicfileno | 电子档案号 | varchar | 50 |  | √ | ' ' | 电子档案号 |
| 20 | fisvirtualnode | 是否为虚拟结点 | varchar | 30 |  | √ | ' ' | 是否为虚拟结点,枚举: 1 :是 2 :否 |
| 21 | fadress | 所在国家/地区 | varchar | 50 |  | √ | ' ' | 所在国家/地区 |
| 22 | parententryid | parententryid | int8 | 64 |  | √ | 0 |  |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fispointcompany | 是否为重点税源企业 | varchar | 30 |  | √ | ' ' | 是否为重点税源企业,枚举: 1 :是 2 :否 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | ftaxername | 纳税人名称 | varchar | 100 |  | √ | ' ' | 纳税人名称 |
| 27 | fcommiterphone | 填表人联系电话 | varchar | 50 |  | √ | ' ' | 填表人联系电话 |
| 28 | fnationtaxsn | 纳税人识别号（国税） | varchar | 50 |  | √ | ' ' | 纳税人识别号（国税） |
| 29 | fcommitername | 填表人姓名 | varchar | 50 |  | √ | ' ' | 填表人姓名 |
| 30 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 31 | fispubliccompany | 是否为上市公司 | varchar | 30 |  | √ | ' ' | 是否为上市公司,枚举: 1 :是 2 :否 |
| 32 | faccountway | 核算方式 | varchar | 50 |  | √ | ' ' | 核算方式 |
| 33 | fstartdate | 有效期起 | timestamp | 0 |  |  | null | 有效期起 |
| 34 | fcodeandnameid | 国标行业（主行业） | int8 | 64 |  | √ | 0 | 行业代码及名称 tpo_tcvat_industrycode |
| 35 | frollstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :未编辑 2 :已编辑 |
| 36 | fgrouproll | 集团名称 | varchar | 100 |  | √ | ' ' | 集团名称 |
| 37 | fregistertype | fregistertype | varchar | 50 |  | √ | ' ' |  |
| 38 | forgname | 组织名称 | varchar | 100 |  | √ | ' ' | 组织名称 |
| 39 | fisvalid | 是否生效 | varchar | 30 |  | √ | ' ' | 是否生效,枚举: 1 :是 2 :否 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fisabroad | 是否为境外企业 | varchar | 30 |  | √ | ' ' | 是否为境外企业,枚举: 1 :是 2 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_group_org_fk |  | fid |
| 2 | pk_t_tcvvt_group_org |  | fentryid |
