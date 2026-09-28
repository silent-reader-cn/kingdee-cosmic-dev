# 数据清理动态配置-wf_cleandynamicconfig

## 数据清理动态配置-主表 t_wf_cleandynamicconfig

- **表名称：** 数据清理动态配置-主表
- **表名：** t_wf_cleandynamicconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcleanmoment | 清理时机 | varchar | 20 |  | √ | ' ' | 清理时机,枚举: immediate :流程结束即时清理 retention :流程结束后定时清理 all :即时清理+定时清理 |
| 3 | fdisposaltype | 数据处理方式 | varchar | 50 |  | √ | ' ' | 数据处理方式,枚举: delete :删除 compact :压缩 |
| 4 | fsteplength | 步长（天） | int4 | 32 |  | √ | 0 | 步长（天） |
| 5 | fentitynumber | 清理实体 | varchar | 36 |  | √ | ' ' | 清理实体 |
| 6 | fparams | 参数集 | varchar | 1000 |  | √ | ' ' | 参数集 |
| 7 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | flimitquantity | 调度处理上限 | int4 | 32 |  | √ | 0 | 调度处理上限 |
| 9 | fretentiontime | 数据保留天数（天） | int4 | 32 |  | √ | 0 | 数据保留天数（天） |
| 10 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 1 :启用 0 :禁用 |
| 11 | fcleanmode | 清理方式 | varchar | 20 |  | √ | ' ' | 清理方式,枚举: process :按流程清理 timing :按保留时间清理 |
| 12 | forder | 执行顺序 | int4 | 32 |  | √ | 0 | 执行顺序 |
| 13 | fsteplimitquantity | 每步处理上限 | int4 | 32 |  | √ | 0 | 每步处理上限 |
| 14 | frelaentity | 清理关联实体 | varchar | 500 |  | √ | ' ' | 清理关联实体 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_cleandynamicconfig |  | fid |
| 2 | idx_wf_cleandyn_entitynumber |  | fentitynumber |
