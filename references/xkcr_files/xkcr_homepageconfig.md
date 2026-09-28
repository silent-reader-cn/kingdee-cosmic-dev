# 看板设置-xkcr_homepageconfig

## 合并范围-多选基础资料表 t_xkcr_homepagescopeentry

- **表名称：** 合并范围-多选基础资料表
- **表名：** t_xkcr_homepagescopeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 合并范围 xkcr_scope |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_homepagescopeentry |  | fpkid |
| 2 | idx_xkcr_homepagescopeentry |  | fentryid |

---

## 单据体-子表 t_xkcr_homepageentry

- **表名称：** 单据体-子表
- **表名：** t_xkcr_homepageentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fconstartwith | 截止日 | varchar | 10 |  | √ | ' ' | 截止日,枚举: 1 :下一期间开始 2 :当前期间结束前 |
| 4 | fconday | 合并范围结束日期 | int8 | 64 |  | √ | 0 | 合并范围结束日期 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_homepageentry |  | fid |
| 2 | pk_t_xkcr_homepageentry |  | fentryid |

---

## 看板设置-主表 t_xkcr_homepageconfig

- **表名称：** 看板设置-主表
- **表名：** t_xkcr_homepageconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsingleday | 个别报表默认结束日期 | int8 | 64 |  | √ | 0 | 个别报表默认结束日期 |
| 3 | flevel | 监控合并范围层级 | varchar | 10 |  | √ | ' ' | 监控合并范围层级,枚举: 1 :当前合并范围 2 :当前合并范围及其所有下级 |
| 4 | fversiongroupid | 合并方案 | int8 | 64 |  | √ | 0 | 合并方案 |
| 5 | fdefaultconstartwith | 默认截止日 | varchar | 10 |  | √ | ' ' | 默认截止日,枚举: 1 :下一期间开始 2 :当前期间结束前 3 :不设置默认 |
| 6 | felimday | 抵销表默认结束日期 | int8 | 64 |  | √ | 0 | 抵销表默认结束日期 |
| 7 | fdefaultconday | 合并报表默认结束日期 | int8 | 64 |  | √ | 0 | 合并报表默认结束日期 |
| 8 | fsinglestartwith | 默认截止日 | varchar | 10 |  | √ | ' ' | 默认截止日,枚举: 1 :下一期间开始 2 :当前期间结束前 |
| 9 | felimstartwith | 默认截止日 | varchar | 10 |  | √ | ' ' | 默认截止日,枚举: 1 :下一期间开始 2 :当前期间结束前 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_homepageconfig |  | fid |
| 2 | idx_xkcr_homepageconfig |  | fversiongroupid |
