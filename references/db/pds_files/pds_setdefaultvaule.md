# 已经设置默认值-pds_setdefaultvaule

## 已经设置默认值-主表 t_pds_setdefaultvaule

- **表名称：** 已经设置默认值-主表
- **表名：** t_pds_setdefaultvaule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdefaultvalueid | 默认值配置ID | int8 | 64 |  | √ | 0 | 默认值配置ID |
| 3 | fbillid | 寻源项目ID | int8 | 64 |  | √ | 0 | 寻源项目ID |
| 4 | fentitykey | 组件实体标识 | varchar | 50 |  | √ | ' ' | 组件实体标识 |
| 5 | fsrctypeid | 寻源流程ID | int8 | 64 |  | √ | 0 | 寻源流程ID |
| 6 | fpentitykey | 父实体标识 | varchar | 50 |  | √ | ' ' | 父实体标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_setdefaultvaule_comp |  | fbillid,fpentitykey,fentitykey,fsrctypeid |
| 2 | pk_pds_setdefaultvaule |  | fid |
