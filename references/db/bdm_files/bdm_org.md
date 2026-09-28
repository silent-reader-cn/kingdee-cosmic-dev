# 企业管理-bdm_org

## 企业管理-主表 t_bdm_org

- **表名称：** 企业管理-主表
- **表名：** t_bdm_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenterprisemainorg | 企业主体组织 | varchar | 10 |  | √ | '0' | 企业主体组织,枚举: 0 :否 1 :是 |
| 3 | fisleaf | fisleaf | varchar | 10 |  | √ | '0' |  |
| 4 | fqrcodestatus | 桌牌二维码状态 | varchar | 10 |  | √ | ' ' | 桌牌二维码状态,枚举: 0 :未生成 1 :已生成 |
| 5 | fdefaultdev | 默认设备 | varchar | 50 |  | √ | ' ' | 默认设备 |
| 6 | fparentname | 上级组织名称 | varchar | 200 |  | √ | ' ' | 上级组织名称 |
| 7 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fepinfo | 企业信息 | int8 | 64 |  | √ | 0 | [企业基础信息 bdm_enterprise_baseinfo](../bdm_files/bdm_enterprise_baseinfo.md) |
| 9 | fstatus | 启用状态 | varchar | 30 |  | √ | ' ' | 启用状态,枚举: A :暂存 B :提交 C :审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | falleaccount | 电子发票服务平台账号 | int8 | 64 |  | √ | 0 | [电子发票服务平台信息 bdm_einvoice_account](../bdm_files/bdm_einvoice_account.md) |
| 13 | fviewtype | 视图类型 | varchar | 50 |  | √ | ' ' | 视图类型 |
| 14 | fname | 组织名称 | varchar | 200 |  | √ | ' ' | 组织名称 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdefaultterminal | 默认终端 | varchar | 50 |  | √ | ' ' | 默认终端 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | flongnumber | 长编码 | varchar | 200 |  | √ | ' ' | 长编码 |
| 19 | fparentbase | fparentbase | int8 | 64 |  | √ | 0 |  |
| 20 | fequipmenttype | fequipmenttype | varchar | 60 |  | √ | ' ' |  |
| 21 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 22 | fdevlist_tag | 设备列表_详情 | text | 0 |  |  | null | 设备列表_详情 |
| 23 | fparent | 上级组织 | varchar | 200 |  | √ | ' ' | 上级组织 |
| 24 | fissuetype | fissuetype | varchar | 60 |  | √ | ' ' |  |
| 25 | fenable | fenable | varchar | 30 |  | √ | ' ' |  |
| 26 | fnumber | 组织编码 | varchar | 50 |  | √ | ' ' | 组织编码 |
| 27 | fdevlist | 设备列表 | varchar | 255 |  | √ | ' ' | 设备列表 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_org |  | fid |
| 2 | idx_bdm_org |  | fnumber |
