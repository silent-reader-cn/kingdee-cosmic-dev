# 模板分发_保存-xkcr_sampledistribute

## 模板分发_保存-主表 t_xkcr_distribute

- **表名称：** 模板分发_保存-主表
- **表名：** t_xkcr_distribute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | frptid | 模板id | varchar | 36 |  | √ | ' ' | 模板id |
| 3 | facctsystemid | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 5 | fnewsampleid | 新模板ID | varchar | 36 |  | √ | ' ' | 新模板ID |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fenable | 可用 | bpchar | 1 |  | √ | '1' | 可用,枚举: 0 :禁用 1 :可用 |
| 8 | fallowedit | 允许修改 | bpchar | 1 |  | √ | ' ' | 允许修改 |
| 9 | fscopetypeid | 合并方案 | int8 | 64 |  | √ | 0 | 合并方案 |
| 10 | fscopeid | 合并范围 | int8 | 64 |  | √ | 0 | 合并范围 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_distribute |  | frptid |
| 2 | pk_xkcr_distribute |  | fid |
