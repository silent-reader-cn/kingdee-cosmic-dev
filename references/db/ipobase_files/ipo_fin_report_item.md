# 财务报表项目-ipo_fin_report_item

## 财务报表项目-多语言表 t_fin_report_item_l

- **表名称：** 财务报表项目-多语言表
- **表名：** t_fin_report_item_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | frptshowname | 报表显示名称 | varchar | 50 |  | √ | ' ' | 报表显示名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fin_report_item_l_0 |  | fid |
| 2 | pk_fin_report_item_l |  | fpkid |

---

## 财务报表项目-主表 t_fin_report_item

- **表名称：** 财务报表项目-主表
- **表名：** t_fin_report_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [IPO财务报表类型 ipo_fin_report_type](../ipobase_files/ipo_fin_report_type.md) |
| 5 | fitemdc | 方向 | varchar | 50 |  | √ | ' ' | 方向,枚举: 1 :借 -1 :贷 |
| 6 | fshowrows | 报表显示行次 | int8 | 64 |  | √ | 0 | 报表显示行次 |
| 7 | frptshowname | 报表显示名称 | varchar | 50 |  | √ | ' ' | 报表显示名称 |
| 8 | fparentid | 父级项目 | int8 | 64 |  | √ | 0 | [财务报表项目 ipo_fin_report_item](../ipobase_files/ipo_fin_report_item.md) |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fdisplayinreport | 是否显示在报表 | bpchar | 1 |  | √ | '1' | 是否显示在报表 |
| 11 | fnotes | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 12 | fistext | 文本项 | bpchar | 1 |  | √ | '0' | 文本项 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcustomptynew | 类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 18 | fdisplayyellow | 是否显示黄色 | bpchar | 1 |  | √ | '0' | 是否显示黄色 |
| 19 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fin_report_item |  | fid |
| 2 | report_item_index |  | fnumber |
