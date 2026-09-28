# 凭证字段自动携带设置-gl_fieldautofill

## 凭证字段自动携带设置-主表 t_gl_fieldautofill

- **表名称：** 凭证字段自动携带设置-主表
- **表名：** t_gl_fieldautofill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmeasureunit | 计量单位 | bpchar | 1 |  | √ | '0' | 计量单位 |
| 3 | foriamount | 原币金额 | bpchar | 1 |  | √ | '0' | 原币金额 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fassgrp | 核算维度 | bpchar | 1 |  | √ | '1' | 核算维度 |
| 6 | fcurrency | 币别 | bpchar | 1 |  | √ | '0' | 币别 |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | faccount | 科目 | bpchar | 1 |  | √ | '0' | 科目 |
| 9 | fprice | 单价 | bpchar | 1 |  | √ | '0' | 单价 |
| 10 | fbusinessnum | 业务编号 | bpchar | 1 |  | √ | '0' | 业务编号 |
| 11 | fexpiredate | 到期日 | bpchar | 1 |  | √ | '0' | 到期日 |
| 12 | fdesc | 摘要 | bpchar | 1 |  | √ | '1' | 摘要 |
| 13 | fquantity | 数量 | bpchar | 1 |  | √ | '0' | 数量 |
| 14 | flocalrate | 汇率 | bpchar | 1 |  | √ | '0' | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_fieldautofill |  | forgid,fuserid |
| 2 | t_gl_fieldautofill_pkey |  | fid |
