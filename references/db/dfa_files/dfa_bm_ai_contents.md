# 指标对比AI解读内容-dfa_bm_ai_contents

## 指标对比AI解读内容-主表 t_dfa_bm_aicontents

- **表名称：** 指标对比AI解读内容-主表
- **表名：** t_dfa_bm_aicontents

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontents_tag | AI解读内容_详情 | text | 0 |  |  | null | AI解读内容_详情 |
| 3 | fcontents | AI解读内容 | varchar | 255 |  | √ | ' ' | AI解读内容 |
| 4 | fuuid | 公司+指标+报告期组合唯一键值 | varchar | 255 |  | √ | ' ' | 公司+指标+报告期组合唯一键值 |
| 5 | fuuiddetails_tag | 公司+指标+报告期组合数据_详情 | text | 0 |  |  | null | 公司+指标+报告期组合数据_详情 |
| 6 | fuuiddetails | 公司+指标+报告期组合数据 | varchar | 255 |  | √ | ' ' | 公司+指标+报告期组合数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_bm_aicontents |  | fid |
| 2 | idx_dfa_bm_aicontents_m0 |  | fuuid |
