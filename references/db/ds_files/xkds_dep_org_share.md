# 星空组织部门结构_共享-xkds_dep_org_share

## 星空组织部门结构_共享-主表 t_ds_dep_org_share

- **表名称：** 星空组织部门结构_共享-主表
- **表名：** t_ds_dep_org_share

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fsrcuseorg | 企业版使用组织ID | varchar | 50 |  | √ | ' ' | 企业版使用组织ID |
| 4 | fmessage | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 5 | fcombonumber | 编码 | varchar | 150 |  | √ | ' ' | 编码 |
| 6 | fcreatetime | 源系统创建时间 | timestamp | 0 |  |  | null | 源系统创建时间 |
| 7 | fuseorg | 使用组织 | varchar | 50 |  | √ | ' ' | 使用组织 |
| 8 | fdescription | 描述 | varchar | 250 |  | √ | ' ' | 描述 |
| 9 | fparentnumber | 上级编码 | varchar | 150 |  | √ | ' ' | 上级编码 |
| 10 | fparentname | 上级名称 | varchar | 150 |  | √ | ' ' | 上级名称 |
| 11 | fmodifytime | 源系统修改时间 | timestamp | 0 |  |  | null | 源系统修改时间 |
| 12 | fcreateorg | 创建组织 | varchar | 50 |  | √ | ' ' | 创建组织 |
| 13 | forgpattern | 形态 | varchar | 50 |  | √ | ' ' | 形态,枚举: 7 :总公司 1 :公司 6 :工厂 3 :事业部 2 :分公司 4 :部门 8 :集团公司 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 Z :暂存 |
| 15 | ftype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: 0 :部门 1 :组织 2 :共享部门 |
| 16 | fparent | 上级 | varchar | 50 |  | √ | ' ' | 上级 |
| 17 | fenable | 禁用状态 | varchar | 50 |  | √ | '1' | 禁用状态,枚举: 0 :是 1 :否 |
| 18 | fnumber | 源系统编码 | varchar | 100 |  | √ | ' ' | 源系统编码 |
| 19 | fsyncstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 0 :未同步 1 :同步成功 2 :同步失败 |
| 20 | fmessage_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 21 | fbillcreatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ds_dep_org_share_number |  | fnumber |
| 2 | pk_t_ds_dep_org_share |  | fid |
