# 静态二维码设置-bdm_qr_code_manage

## 静态二维码设置-主表 t_bdm_org

- **表名称：** 静态二维码设置-主表
- **表名：** t_bdm_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenterprisemainorg | fenterprisemainorg | varchar | 10 |  | √ | '0' |  |
| 3 | fisleaf | fisleaf | varchar | 10 |  | √ | '0' |  |
| 4 | fqrcodestatus | 桌牌二维码状态 | varchar | 10 |  | √ | ' ' | 桌牌二维码状态,枚举: 0 :未生成 1 :已生成 |
| 5 | fdefaultdev | fdefaultdev | varchar | 50 |  | √ | ' ' |  |
| 6 | fparentname | fparentname | varchar | 200 |  | √ | ' ' |  |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | 企业基础信息 bdm_enterprise_baseinfo |
| 9 | fstatus | fstatus | varchar | 30 |  | √ | ' ' |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | falleaccount | falleaccount | int8 | 64 |  | √ | 0 |  |
| 13 | fviewtype | fviewtype | varchar | 50 |  | √ | ' ' |  |
| 14 | fname | 组织名称 | varchar | 200 |  | √ | ' ' | 组织名称 |
| 15 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 16 | fdefaultterminal | fdefaultterminal | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 18 | flongnumber | flongnumber | varchar | 200 |  | √ | ' ' |  |
| 19 | fparentbase | fparentbase | int8 | 64 |  | √ | 0 |  |
| 20 | fequipmenttype | fequipmenttype | varchar | 60 |  | √ | ' ' |  |
| 21 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 22 | fdevlist_tag | fdevlist_tag | text | 0 |  |  | null |  |
| 23 | fparent | fparent | varchar | 200 |  | √ | ' ' |  |
| 24 | fissuetype | fissuetype | varchar | 60 |  | √ | ' ' |  |
| 25 | fenable | fenable | varchar | 30 |  | √ | ' ' |  |
| 26 | fnumber | 组织编码 | varchar | 50 |  | √ | ' ' | 组织编码 |
| 27 | fdevlist | fdevlist | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_org |  | fid |
| 2 | idx_bdm_org |  | fnumber |
