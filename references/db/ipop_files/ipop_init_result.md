# 初始化标记结果-ipop_init_result

## 初始化标记结果-主表 t_ipop_init_result

- **表名称：** 初始化标记结果-主表
- **表名：** t_ipop_init_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 完成状态 | varchar | 10 |  | √ | ' ' | 完成状态,枚举: 0 :未完成 1 :已完成 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fitemid | 初始化事项 | int8 | 64 |  | √ | 0 | 初始化事项配置 ipop_init_itemcfg |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_init_result |  | fid |
| 2 | idx_ipop_init_result_item |  | fitemid |
| 3 | idx_ipop_init_result_org |  | forgid |
