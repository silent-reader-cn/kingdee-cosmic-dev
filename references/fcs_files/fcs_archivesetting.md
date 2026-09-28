# 归档配置-fcs_archivesetting

## 归档配置-主表 t_fcs_archivesetting

- **表名称：** 归档配置-主表
- **表名：** t_fcs_archivesetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | farchivemincnt | 归档最小数据量 | int4 | 32 |  | √ | 0 | 归档最小数据量 |
| 3 | fname | 名称 | varchar | 60 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftimeprop | 时间字段 | varchar | 60 |  | √ | ' ' | 时间字段,枚举: |
| 7 | farchivedel | 开启归档删除 | bpchar | 1 |  | √ | '0' | 开启归档删除 |
| 8 | fsrctypeid | 源单类型 | varchar | 60 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 9 | flivetime | 存活时间(小时) | int4 | 32 |  | √ | 0 | 存活时间(小时) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | farchiveliveday | 归档保留天数 | int4 | 32 |  | √ | 0 | 归档保留天数 |
| 15 | farchivefilter | 归档过滤条件 | varchar | 255 |  | √ | ' ' | 归档过滤条件 |
| 16 | farchivetypeid | 归档单类型 | varchar | 60 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fday | 归档时间(天) | int4 | 32 |  | √ | 0 | 归档时间(天) |
| 19 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 20 | farchivefilter_tag | 归档过滤条件_详情 | text | 0 |  |  | null | 归档过滤条件_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_archivesetting_num |  | fnumber |
| 2 | pk_t_fcs_archivesetting |  | fid |

---

## 归档配置-多语言表 t_fcs_archivesetting_l

- **表名称：** 归档配置-多语言表
- **表名：** t_fcs_archivesetting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 60 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fcs_archivesetting_l_fid |  | fid |
| 2 | pk_t_fcs_archivesetting_l |  | fpkid |
