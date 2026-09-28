# 项目映射关系-tdm_item_mapping

## 项目映射关系-主表 t_tdm_item_mapping

- **表名称：** 项目映射关系-主表
- **表名：** t_tdm_item_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdatasrc | 集成系统 | varchar | 50 |  | √ | ' ' | 集成系统,枚举: hbbb :星瀚合并报表 cwbb :星瀚财务报表 zzbb :星瀚总账 merge :EAS合并报表 xkqjcwbb :星空旗舰财务报表 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fitemtype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: tdm_item_zcfzb :资产负债表项目 tdm_item_xjllb :现金流量表项目 tdm_item_lrb :利润表项目 tdm_item_qybdb :所有者权益变动表项目 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fissystem | 系统预设 | varchar | 50 |  | √ | ' ' | 系统预设,枚举: 0 :否 1 :是 |
| 12 | fitem | 报表项目 | int8 | 64 |  | √ | 0 | 资产负债表项目 tdm_item_zcfzb |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_item_mapping |  | fid |
| 2 | idx_tdm_item_mapping |  | fnumber |

---

## 项目映射关系-多语言表 t_tdm_item_mapping_l

- **表名称：** 项目映射关系-多语言表
- **表名：** t_tdm_item_mapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_item_mapping_l |  | fpkid |
| 2 | idx_tdm_item_mapping_l_0 |  | fid,flocaleid |
