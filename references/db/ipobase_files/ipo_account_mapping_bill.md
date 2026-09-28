# 取数科目映射单据-ipo_account_mapping_bill

## 会计科目-多选基础资料表 t_theme_account_mapping_a

- **表名称：** 会计科目-多选基础资料表
- **表名：** t_theme_account_mapping_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_theme_account_mapping_a_fk |  | fid |
| 2 | pk_theme_account_mapping_a |  | fpkid |

---

## 取数科目映射单据-主表 t_theme_account_mapping

- **表名称：** 取数科目映射单据-主表
- **表名：** t_theme_account_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcountry_tag | 地区_详情 | text | 0 |  |  | '' | 地区_详情 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fanalitemld | IPO主题分析表科目 | int8 | 64 |  | √ | 0 | [IPO主题分析表科目 ipo_theme_anal_item](../ipobase_files/ipo_theme_anal_item.md) |
| 7 | faccounttype | 科目类型 | varchar | 50 |  | √ | ' ' | 科目类型,枚举: 0 :科目 1 :科目+核算维度 2 :科目范围 3 :报表项目 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fipoorgld | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 10 | fcountry | 地区 | varchar | 255 |  | √ | ' ' | 地区 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | account_mapping_index |  | fipoorgld |
| 2 | pk_theme_account_mapping |  | fid |

---

## 核算维度-多选基础资料表 t_theme_account_mapping_t

- **表名称：** 核算维度-多选基础资料表
- **表名：** t_theme_account_mapping_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_account_mapping_t |  | fpkid |
| 2 | idx_theme_account_mapping_t_fk |  | fid |
