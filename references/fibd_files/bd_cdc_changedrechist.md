# 待处理变动记录历史表-bd_cdc_changedrechist

## 待处理变动记录历史表-主表 t_bd_cdc_changedrechist

- **表名称：** 待处理变动记录历史表-主表
- **表名：** t_bd_cdc_changedrechist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :新增 9 :删除 |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 6 | fopertype | 变动类型 | bpchar | 1 |  | √ | '1' | 变动类型,枚举: 1 :新增或变动 2 :删除 |
| 7 | fsrcrecid | 目标记录ID | int8 | 64 |  | √ | 0 | 目标记录ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_cdc_changedrechist |  | fid |
| 2 | idx_bd_cdc_changedrechist_1 |  | forgid,fperiodid,fid,fstatus |
