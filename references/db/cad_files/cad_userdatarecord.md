# 用户数据记录-cad_userdatarecord

## 用户数据记录-主表 t_cad_userdatarecord

- **表名称：** 用户数据记录-主表
- **表名：** t_cad_userdatarecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffinishcalwizardsrate | 完工产品结算差异率 | varchar | 50 |  | √ | ' ' | 完工产品结算差异率 |
| 3 | fconforcostreduct | 条件-实际成本还原 | varchar | 2000 |  | √ | ' ' | 条件-实际成本还原 |
| 4 | faudittoconfirm | 更新申请单审核后直接进入确认单 | bpchar | 1 |  | √ | '0' | 更新申请单审核后直接进入确认单 |
| 5 | fcondition | 条件-完工json | varchar | 2000 |  | √ | ' ' | 条件-完工json |
| 6 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | funconfirmnottip | 成本确认单不再提示反确认 | bpchar | 1 |  | √ | '0' | 成本确认单不再提示反确认 |
| 8 | fconfirmnottip | 成本确认单不再提示确认 | bpchar | 1 |  | √ | '0' | 成本确认单不再提示确认 |
| 9 | fautoendperiodcal | 更新前自动执行期末成本计算 | bpchar | 1 |  | √ | '1' | 更新前自动执行期末成本计算 |
| 10 | fconditionforend | 条件-期末json | varchar | 2000 |  | √ | ' ' | 条件-期末json |
| 11 | fmodifytime | 记录时间 | timestamp | 0 |  |  | null | 记录时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_userdatarecord |  | fuserid |
| 2 | t_cad_userdatarecord_pkey |  | fid |
