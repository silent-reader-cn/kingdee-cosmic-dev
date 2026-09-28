# 内部交易单据默认仓库（存储）-ism_defaultorgwarehouse

## 内部交易单据默认仓库（存储）-主表 t_ism_defaultorgwarehouse

- **表名称：** 内部交易单据默认仓库（存储）-主表
- **表名：** t_ism_defaultorgwarehouse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | forgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | flocation | 默认仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 6 | fwarehouseid | 默认仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_defaultorgwarehouse |  | fid |
