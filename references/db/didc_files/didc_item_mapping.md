# 报表项目映射-didc_item_mapping

## 报表项目映射-主表 t_didc_item_mapping

- **表名称：** 报表项目映射-主表
- **表名：** t_didc_item_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftenant | 租户数据中心 | int8 | 64 |  | √ | 0 | 租户数据中心 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [IPO财务报表类型 ipo_fin_report_type](../ipobase_files/ipo_fin_report_type.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ffinreportitem | 财务报表项目 | int8 | 64 |  | √ | 0 | [财务报表项目 ipo_fin_report_item](../ipobase_files/ipo_fin_report_item.md) |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fitemnumber | 映射项目编码 | varchar | 255 |  | √ | ' ' | 映射项目编码 |
| 13 | fitemsgroup | 集成报表项目分组 | int8 | 64 |  | √ | 0 | [报表项目分组 didc_itemsgroup](../didc_files/didc_itemsgroup.md) |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fitemname | 映射项目名称 | varchar | 255 |  | √ | ' ' | 映射项目名称 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_item_mapping_m0 |  | fmasterid |
| 2 | pk_didc_item_mapping |  | fid |

---

## 报表项目映射-多语言表 t_didc_item_mapping_l

- **表名称：** 报表项目映射-多语言表
- **表名：** t_didc_item_mapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_item_mapping_l_0 |  | fid,flocaleid |
| 2 | pk_didc_item_mapping_l |  | fpkid |
