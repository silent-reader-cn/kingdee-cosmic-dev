# 预算汇总表设置-xkbm_sumrptsetting

## 预算汇总表设置-主表 t_xkbm_sumrptsetting

- **表名称：** 预算汇总表设置-主表
- **表名：** t_xkbm_sumrptsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffirstgroupsum | 第一个行维度分组汇总字段： | bpchar | 1 |  | √ | '0' | 第一个行维度分组汇总字段： |
| 3 | fendperiod | 结束期间 | varchar | 30 |  | √ | ' ' | 结束期间,枚举: |
| 4 | forderdimtype | 排序维度 | varchar | 100 |  | √ | ' ' | 排序维度,枚举: |
| 5 | fincludenoneleaforg | 包含下级非明细组织 | bpchar | 1 |  | √ | '0' | 包含下级非明细组织 |
| 6 | fincludecurorg | 包含当前组织 | bpchar | 1 |  | √ | '0' | 包含当前组织 |
| 7 | ffirstgroupsumfield | 分组汇总字段 | varchar | 30 |  | √ | ' ' | 分组汇总字段,枚举: 1 :维度名称 2 :维度编码 |
| 8 | fsumschemeid | 汇总表样式方案 | int8 | 64 |  | √ | 0 | [预算汇总样式方案 xkbm_sumrptscheme](../xkbm_files/xkbm_sumrptscheme.md) |
| 9 | fstartperiod | 开始期间 | varchar | 30 |  | √ | ' ' | 开始期间,枚举: |
| 10 | fendyear | 结束年度 | varchar | 30 |  | √ | ' ' | 结束年度,枚举: |
| 11 | fisnotshowzero | 预算数为零不显示 | bpchar | 1 |  | √ | '0' | 预算数为零不显示 |
| 12 | fstartyear | 开始年度 | varchar | 30 |  | √ | ' ' | 开始年度,枚举: |
| 13 | fcycles | 报表包含周期 | varchar | 255 |  | √ | ' ' | 报表包含周期,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 14 | fincludeunauditreport | 包含未审核的报表 | bpchar | 1 |  | √ | '1' | 包含未审核的报表 |
| 15 | fisnotshowfinalzero | 结果数为零不显示 | bpchar | 1 |  | √ | '0' | 结果数为零不显示 |
| 16 | fordertype | 维度排序方式 | varchar | 30 |  | √ | ' ' | 维度排序方式,枚举: 1 :维度名称 2 :维度编码 |
| 17 | fisadjust | 包含预算调整数 | bpchar | 1 |  | √ | '0' | 包含预算调整数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_sumrptsetting |  | fsumschemeid |
| 2 | pk_xkbm_sumrptsetting |  | fid |
