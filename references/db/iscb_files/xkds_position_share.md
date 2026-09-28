# 岗位同步中间表_共享-xkds_position_share

## 岗位同步中间表_共享-主表 t_xkds_position_share

- **表名称：** 岗位同步中间表_共享-主表
- **表名：** t_xkds_position_share

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ftardept | 目标系统所属部门 | int8 | 64 |  | √ | 0 | 目标系统所属部门 |
| 4 | fuseorg | 使用组织 | varchar | 50 |  | √ | ' ' | 使用组织 |
| 5 | fcreatetime | 源系统创建时间 | timestamp | 0 |  |  | null | 源系统创建时间 |
| 6 | fcombonumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 7 | fdept | 源系统所属部门 | varchar | 50 |  | √ | ' ' | 源系统所属部门 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fcreateorg | 创建组织 | varchar | 50 |  | √ | ' ' | 创建组织 |
| 10 | fmodifytime | 源系统修改时间 | timestamp | 0 |  |  | null | 源系统修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 Z :暂存 |
| 12 | ftype | 数据类型 | varchar | 50 |  | √ | '0' | 数据类型,枚举: 0 :岗位 1 :共享岗位 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 源系统编码 | varchar | 100 |  | √ | ' ' | 源系统编码 |
| 15 | fbillcreatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_positions_useorg |  | fuseorg |
| 2 | pk_xkds_position_share |  | fid |
| 3 | idx_positions_creorg |  | fcreateorg |
