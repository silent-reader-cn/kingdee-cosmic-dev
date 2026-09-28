# 实物卡片业务流程控制-fa_card_biz_ctr

## 实物卡片业务流程控制-主表 t_fa_card_biz_ctr

- **表名称：** 实物卡片业务流程控制-主表
- **表名：** t_fa_card_biz_ctr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillid | 源单据id | int8 | 64 |  | √ | 0 | 源单据id |
| 3 | fsrcbillentityname | 源单据标识 | varchar | 30 |  | √ | 'NOENTITYNAME' | 源单据标识 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_card_biz_ctr |  | fsrcbillentityname,fsrcbillid |
| 2 | pk_t_fa_card_biz_ctr |  | fid |
