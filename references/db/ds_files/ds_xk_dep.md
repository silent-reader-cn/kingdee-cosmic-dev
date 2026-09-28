# 星空部门中间表-ds_xk_dep

## 星空部门中间表-主表 t_ds_xk_dep

- **表名称：** 星空部门中间表-主表
- **表名：** t_ds_xk_dep

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcreatetime | 星空创建时间 | timestamp | 0 |  |  | null | 星空创建时间 |
| 4 | fuseorg | 使用组织 | varchar | 50 |  | √ | ' ' | 使用组织 |
| 5 | fcreateorgname | 创建组织名称 | varchar | 50 |  | √ | ' ' | 创建组织名称 |
| 6 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 7 | fuseorgnumber | 使用组织编码 | varchar | 50 |  | √ | ' ' | 使用组织编码 |
| 8 | fparentnumber | 上级部门编码 | varchar | 150 |  | √ | ' ' | 上级部门编码 |
| 9 | fparentname | 上级部门名称 | varchar | 150 |  | √ | ' ' | 上级部门名称 |
| 10 | fmodifytime | 星空修改时间 | timestamp | 0 |  |  | null | 星空修改时间 |
| 11 | fcreateorg | 创建组织 | varchar | 50 |  | √ | ' ' | 创建组织 |
| 12 | fcreateorgnumber | 创建组织编码 | varchar | 50 |  | √ | ' ' | 创建组织编码 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :创建 B :审核中 C :已审核 D :待审核 Z :暂存 |
| 14 | fuseorgname | 使用组织名称 | varchar | 50 |  | √ | ' ' | 使用组织名称 |
| 15 | fparent | 上级部门 | varchar | 50 |  | √ | ' ' | 上级部门 |
| 16 | fenable | 禁用状态 | varchar | 50 |  | √ | ' ' | 禁用状态,枚举: A :否 B :是 |
| 17 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ds_xk_dep |  | fnumber |
| 2 | pk_t_ds_xk_dep |  | fid |
