# 映射适用组织(单据)-fah_valmap_type_org

## 映射适用组织(单据)-主表 t_fah_valmap_type_org

- **表名称：** 映射适用组织(单据)-主表
- **表名：** t_fah_valmap_type_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fiscustom | 个性化标识 | bpchar | 1 |  | √ | ' ' | 个性化标识 |
| 3 | fmaptypeid | 映射类型id | int8 | 64 |  | √ | 0 | 映射类型id |
| 4 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fownorgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | forgtype | 适用组织类型 | varchar | 2 |  | √ | ' ' | 适用组织类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fah_valmap_type_org |  | fmaptypeid |
| 2 | pk_fah_valmap_type_org |  | fid |
