# 配置BOM条件关系表单-plm_conf_con_relation

## 单据体-子表 t_plm_cof_con_relation

- **表名称：** 单据体-子表
- **表名：** t_plm_cof_con_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmerge_display | 合成属性显示 | varchar | 255 |  | √ | ' ' | 合成属性显示 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fconditions_tag | 配置变量条件_详情 | text | 0 |  |  | null | 配置变量条件_详情 |
| 5 | fchoose_conditions_tag | 命中变量条件_详情 | text | 0 |  |  | null | 命中变量条件_详情 |
| 6 | fconditions_display_tag | 变量条件_详情 | text | 0 |  |  | null | 变量条件_详情 |
| 7 | fchoose_conditions | 命中变量条件 | varchar | 255 |  | √ | ' ' | 命中变量条件 |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fconditions_display | 变量条件 | varchar | 255 |  | √ | ' ' | 变量条件 |
| 11 | fmerge_condition_tag | 合成属性条件_详情 | text | 0 |  |  | null | 合成属性条件_详情 |
| 12 | flogic_condition | 逻辑条件 | varchar | 50 |  | √ | ' ' | 逻辑条件,枚举: 1 :满足所有条件 2 :满足任意条件 3 :自定义 |
| 13 | fmerge_condition_display | 合成属性条件显示 | varchar | 255 |  | √ | ' ' | 合成属性条件显示 |
| 14 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 15 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 16 | fbom_entryid | BOMentryId | int8 | 64 |  | √ | 0 | BOMentryId |
| 17 | fmerge_condition | 合成属性条件 | varchar | 255 |  | √ | ' ' | 合成属性条件 |
| 18 | fchoose_conditions_disp | 数量条件 | varchar | 255 |  | √ | ' ' | 数量条件 |
| 19 | fmerge | 合成属性 | varchar | 255 |  | √ | ' ' | 合成属性 |
| 20 | fmerge_tag | 合成属性_详情 | text | 0 |  |  | null | 合成属性_详情 |
| 21 | fmerge_display_tag | 合成属性显示_详情 | text | 0 |  |  | null | 合成属性显示_详情 |
| 22 | fmerge_condition_display_tag | 合成属性条件显示_详情 | text | 0 |  |  | null | 合成属性条件显示_详情 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fconditions | 配置变量条件 | varchar | 255 |  | √ | ' ' | 配置变量条件 |
| 25 | fchoose_conditions_disp_tag | 数量条件_详情 | text | 0 |  |  | null | 数量条件_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_cof_con_relation |  | fid |
| 2 | pk_t_plm_cof_con_relation |  | fentryid |

---

## 配置BOM条件关系表单-主表 t_plm_cof_con_main

- **表名称：** 配置BOM条件关系表单-主表
- **表名：** t_plm_cof_con_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fbomid | BOM版本ｉｄ | int8 | 64 |  | √ | 0 | BOM版本ｉｄ |
| 4 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_cof_con_main |  | fid |
| 2 | idx_t_plm_cof_con_main |  | fbomid |
