# IPO主题分析表取数来源单据-ipo_anal_datasourse

## 期间-多选基础资料表 t_theme_anal_period

- **表名称：** 期间-多选基础资料表
- **表名：** t_theme_anal_period

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [会计期间 ds_period](../ds_files/ds_period.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_anal_period |  | fpkid |
| 2 | idx_theme_anal_period_fk |  | fid |

---

## IPO主题分析表取数来源单据-主表 t_ipo_anal_datasourse

- **表名称：** IPO主题分析表取数来源单据-主表
- **表名：** t_ipo_anal_datasourse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fipo_org | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 3 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :取合并报表模块合并财务报表 2 :取EXECL导入财务报表 3 :优先取合并报表模块，取不到时取EXECL导入 |
| 4 | fapp_code | 应用编码 | varchar | 50 |  | √ | ' ' | 应用编码 |
| 5 | fipo_report_code | IPO报表标识 | varchar | 50 |  | √ | ' ' | IPO报表标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ipo_anal_datasourse |  | fid |
| 2 | anal_datasourse_index |  | fipo_org |
