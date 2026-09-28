# 数据源配置-mrp_resource_dataconf_rgt

## 数据源配置-主表 t_mrp_rsdataconfig

- **表名称：** 数据源配置-主表
- **表名：** t_mrp_rsdataconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcgnumber | 资源注册配置编码 | int8 | 64 |  | √ | 0 | 资源注册模型 mrp_resourceregister_cf |
| 3 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fissystemdesign | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | ftype | ftype | varchar | 30 |  | √ | ' ' |  |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | flargetextfield_tag | 目标实体条件存储_详情 | text | 0 |  |  | null | 目标实体条件存储_详情 |
| 15 | fsourcetype | 应用来源 | varchar | 10 |  | √ | 'mrp' | 应用来源 |
| 16 | fbillfieldtransferid | 实体字段映射 | int8 | 64 |  | √ | 0 | 实体字段映射 mrp_billfieldtransfer |
| 17 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 18 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | flargetextfield | 目标实体条件存储 | varchar | 255 |  | √ | ' ' | 目标实体条件存储 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 23 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_rsdataconfig |  | fid |
| 2 | idx_mrp_rsdataconfig |  | fnumber,fcreateorgid |

---

## 数据源配置-多语言表 t_mrp_rsdataconfig_l

- **表名称：** 数据源配置-多语言表
- **表名：** t_mrp_rsdataconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_rsdataconfig_l |  | fpkid |
| 2 | idx_mrp_rsdataconfig_l |  | fid,flocaleid |
