# 元素核对结果-tdm_ele_check_plan_res

## 核对详情-子表 t_tdm_ele_check_res_entry

- **表名称：** 核对详情-子表
- **表名：** t_tdm_ele_check_res_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feleruntime | 元素计算时间 | timestamp | 0 |  |  | null | 元素计算时间 |
| 3 | fdiff | 核对差异值 | varchar | 50 |  | √ | ' ' | 核对差异值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fenddata | 计算时间止 | timestamp | 0 |  |  | null | 计算时间止 |
| 6 | forg | 运行组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ferrorreport | 错误报告 | varchar | 255 |  | √ | ' ' | 错误报告 |
| 8 | fcurval | 元素结果值 | varchar | 50 |  | √ | ' ' | 元素结果值 |
| 9 | fele | 元素 | int8 | 64 |  | √ | 0 | 元素设置 tdm_element_group |
| 10 | fformula | 复核元素表达式 | varchar | 2000 |  | √ | ' ' | 复核元素表达式 |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 12 | fstartdata | 计算时间起 | timestamp | 0 |  |  | null | 计算时间起 |
| 13 | ferrorreport_tag | 错误报告_详情 | text | 0 |  |  | null | 错误报告_详情 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fchildrentotal | 下级元素复核汇总值 | varchar | 50 |  | √ | ' ' | 下级元素复核汇总值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_ele_check_res_entry |  | fentryid |
| 2 | idx_tdm_ele_check_res_entry_fk |  | fid |

---

## 元素核对结果-主表 t_tdm_ele_check_plan_res

- **表名称：** 元素核对结果-主表
- **表名：** t_tdm_ele_check_plan_res

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrorelemsg | 错误顶层元素详情 | varchar | 255 |  | √ | ' ' | 错误顶层元素详情 |
| 3 | fisrecal | 是否重算 | varchar | 50 |  | √ | ' ' | 是否重算,枚举: 1 :是 0 :否 |
| 4 | funnormalcount | 核对不匹配数 | int8 | 64 |  | √ | 0 | 核对不匹配数 |
| 5 | ferrorelemsg_tag | 错误顶层元素详情_详情 | text | 0 |  |  | null | 错误顶层元素详情_详情 |
| 6 | fplanno | 核对方案编码 | varchar | 50 |  | √ | ' ' | 核对方案编码 |
| 7 | fplanname | 核对方案名称 | varchar | 50 |  | √ | ' ' | 核对方案名称 |
| 8 | fruntime | 核对运行时间 | timestamp | 0 |  |  | null | 核对运行时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_ele_check_plan_res |  | fid |
| 2 | idx_tdm_ele_check_plan_res |  | fplanno |
