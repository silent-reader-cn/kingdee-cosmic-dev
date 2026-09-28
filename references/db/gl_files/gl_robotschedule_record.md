# 结账机器人回调结果-gl_robotschedule_record

## 结账机器人回调结果-主表 t_gl_rpaschedulerecord

- **表名称：** 结账机器人回调结果-主表
- **表名：** t_gl_rpaschedulerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计期间 |
| 3 | fexecuteresult | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 0 :默认 1 :成功 2 :失败 |
| 4 | fclosedetail | 执行失败详情 | varchar | 510 |  | √ | ' ' | 执行失败详情 |
| 5 | fclosebiz | 执行模块 | varchar | 28 |  | √ | ' ' | 执行模块 |
| 6 | frpacode | 机器人编码 | varchar | 28 |  | √ | ' ' | 机器人编码 |
| 7 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | 账簿 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rpascherecord_fbookid |  | fbookid |
| 2 | pk_gl_rpaschedulerecord |  | fid |
