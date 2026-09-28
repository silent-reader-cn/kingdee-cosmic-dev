# 库房结构设置（已废弃）-eafc_store_config

## 区域单据体-子表 tk_eafc_store_area_config

- **表名称：** 区域单据体-子表
- **表名：** tk_eafc_store_area_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_part_num | 单层节数 | int8 | 64 |  |  | null | 单层节数 |
| 3 | fk_eafc_area_name | 区域名称 | varchar | 50 |  | √ | ' ' | 区域名称 |
| 4 | fk_eafc_floor_num | 单面层数 | int8 | 64 |  |  | null | 单面层数 |
| 5 | fk_eafc_part_width | 预设宽度 | numeric | 23 | 10 |  | null | 预设宽度 |
| 6 | fk_eafc_is_pre_box_num | 是否预设装盒数 | bpchar | 1 |  | √ | '0' | 是否预设装盒数 |
| 7 | fk_eafc_right_no | 右侧编码 | varchar | 50 |  | √ | ' ' | 右侧编码 |
| 8 | fk_eafc_area_shelf_num | 放置密集架组数 | int8 | 64 |  |  | null | 放置密集架组数 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fk_eafc_area_no | 区域编码 | varchar | 50 |  | √ | ' ' | 区域编码 |
| 11 | fk_eafc_area_status | 区域状态 | varchar | 50 |  | √ | ' ' | 区域状态,枚举: 1 :在用 0 :未用 |
| 12 | fk_eafc_box_standard | 规格 | varchar | 50 |  | √ | ' ' | 规格,枚举: 20 :20mm 40 :40mm 60 :60mm |
| 13 | fk_eafc_part_box_num | 预设装盒数 | int8 | 64 |  |  | null | 预设装盒数 |
| 14 | fk_eafc_area_area | 区域面积 | numeric | 23 | 2 |  | null | 区域面积 |
| 15 | fk_eafc_left_no | 左侧编码 | varchar | 50 |  | √ | ' ' | 左侧编码 |
| 16 | fk_eafc_shelf_side | 首尾柜子 | varchar | 50 |  | √ | ' ' | 首尾柜子,枚举: 1 :单面 2 :双面 |
| 17 | fk_eafc_one_side | 是否单面 | bpchar | 1 |  | √ | '0' | 是否单面 |
| 18 | fk_eafc_area_desc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 20 | fk_eafc_shelf_no_end | 密集架编号结束 | int8 | 64 |  |  | null | 密集架编号结束 |
| 21 | fk_eafc_shelf_no_start | 密集架编号开始 | int8 | 64 |  |  | null | 密集架编号开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_store_area_config |  | fentryid |

---

## 库房结构设置（已废弃）-主表 tk_eafc_store_config

- **表名称：** 库房结构设置（已废弃）-主表
- **表名：** tk_eafc_store_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
