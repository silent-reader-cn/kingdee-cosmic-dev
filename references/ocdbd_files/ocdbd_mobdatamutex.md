# 移动端网控监控-ocdbd_mobdatamutex

## 移动端网控监控-主表 t_ocdbd_mobdatamutex

- **表名称：** 移动端网控监控-主表
- **表名：** t_ocdbd_mobdatamutex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fistaskdeletemutex | 是否调度任务删除网控 | bpchar | 1 |  | √ | '0' | 是否调度任务删除网控 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fsrcbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 6 | fexpirydate | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 7 | fsrcentity | 来源单据 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_mobdatamutex |  | fid |
| 2 | idx_ocdbd_mobdatamutex |  | fsrcbillid |
