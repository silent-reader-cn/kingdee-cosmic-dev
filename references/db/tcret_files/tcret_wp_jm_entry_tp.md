# 尾盘销售税源减免(暂存)-tcret_wp_jm_entry_tp

## 尾盘销售税源减免(暂存)-主表 t_tcret_wp_jm_entry_tp

- **表名称：** 尾盘销售税源减免(暂存)-主表
- **表名：** t_tcret_wp_jm_entry_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhoutype | 房屋类型 | varchar | 50 |  | √ | ' ' | 房屋类型,枚举: |
| 3 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 4 | fsbbid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 5 | ftaxdeduction | 减免项目名称及代码 | int8 | 64 |  | √ | 0 | 减免政策代码 tpo_taxdeduction |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcret_wp_jm_entry_tp1 |  | fsbbid,fhoutype |
| 2 | pk_tcret_wp_jm_entry_tp |  | fid |
