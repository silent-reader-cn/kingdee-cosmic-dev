# 元素仓库-tdm_element_result

## 元素仓库-主表 t_tdm_element_result

- **表名称：** 元素仓库-主表
- **表名：** t_tdm_element_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 元素名称 | varchar | 100 |  | √ | ' ' | 元素名称 |
| 3 | felestartdate | 取数属期起 | timestamp | 0 |  |  | null | 取数属期起 |
| 4 | felement | 元素编码 | varchar | 100 |  | √ | ' ' | 元素编码 |
| 5 | fenddata | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | fcaltype | fcaltype | varchar | 30 |  | √ | ' ' |  |
| 7 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fisdenominatorzero | 是否存在分母为零 | bpchar | 1 |  | √ | ' ' | 是否存在分母为零 |
| 9 | fusetype | 使用场景 | varchar | 50 |  | √ | '0' | 使用场景,枚举: 0 :税务风险管控 1 :税务元素 |
| 10 | fvalue | 值 | varchar | 100 |  | √ | ' ' | 值 |
| 11 | fisdisplay | fisdisplay | varchar | 30 |  | √ | ' ' |  |
| 12 | fisemptyfield | 字段是否为空 | bpchar | 1 |  | √ | ' ' | 字段是否为空 |
| 13 | fstartdata | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 14 | feleenddate | 取数属期止 | timestamp | 0 |  |  | null | 取数属期止 |
| 15 | fruntime | 计算时间 | timestamp | 0 |  |  | null | 计算时间 |
| 16 | felementdef | 元素 | int8 | 64 |  | √ | 0 | 元素设置 tdm_element_group |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_element_result_pkey |  | fid |
| 2 | idx_tdm_element_result |  | forg,fstartdata,fenddata,felement |
