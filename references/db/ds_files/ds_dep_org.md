# 星空组织部门结构-ds_dep_org

## 星空组织部门结构-主表 t_ds_dep_org

- **表名称：** 星空组织部门结构-主表
- **表名：** t_ds_dep_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmessage | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 4 | fcreatetime | 源系统创建时间 | timestamp | 0 |  |  | null | 源系统创建时间 |
| 5 | fuseorg | 使用组织 | varchar | 50 |  | √ | ' ' | 使用组织 |
| 6 | fcombonumber | 编码 | varchar | 150 |  | √ | ' ' | 编码 |
| 7 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 8 | fparentnumber | 上级编码 | varchar | 150 |  | √ | ' ' | 上级编码 |
| 9 | fparentname | 上级名称 | varchar | 150 |  | √ | ' ' | 上级名称 |
| 10 | fmodifytime | 源系统修改时间 | timestamp | 0 |  |  | null | 源系统修改时间 |
| 11 | fcreateorg | 创建组织 | varchar | 50 |  | √ | ' ' | 创建组织 |
| 12 | forgpattern | 形态 | varchar | 50 |  | √ | ' ' | 形态,枚举: 7 :总公司 1 :公司 6 :工厂 3 :事业部 2 :分公司 4 :部门 8 :集团公司 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 Z :暂存 |
| 14 | ftype | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型,枚举: 0 :部门 1 :组织 |
| 15 | fparent | 上级 | varchar | 50 |  | √ | ' ' | 上级 |
| 16 | fenable | 禁用状态 | varchar | 50 |  | √ | ' ' | 禁用状态,枚举: 0 :是 1 :否 |
| 17 | fnumber | 源系统编码 | varchar | 100 |  | √ | ' ' | 源系统编码 |
| 18 | fmessage_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 19 | fsyncstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 0 :未同步 1 :同步成功 2 :同步失败 |
| 20 | fbillcreatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ds_dep_org |  | fid |
| 2 | idx_ds_orgdep_key |  | fnumber |
