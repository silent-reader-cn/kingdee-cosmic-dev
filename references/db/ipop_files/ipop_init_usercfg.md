# 初始化事项负责人-ipop_init_usercfg

## 初始化事项负责人-主表 t_ipop_init_usercfg

- **表名称：** 初始化事项负责人-主表
- **表名：** t_ipop_init_usercfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcustomer | 甲方负责人 | varchar | 100 |  | √ | ' ' | 甲方负责人 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fadviser | 实施顾问 | varchar | 100 |  | √ | ' ' | 实施顾问 |
| 8 | fitemid | 初始化事项 | int8 | 64 |  | √ | 0 | 初始化事项配置 ipop_init_itemcfg |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_init_usercfg |  | fid |
| 2 | idx_ipop_init_usercfg_item |  | fitemid |
| 3 | idx_ipop_init_usercfg_org |  | forgid |
