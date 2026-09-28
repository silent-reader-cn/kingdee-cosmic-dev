# 开发土地信息-tdm_develop_land_info

## 开发土地信息-多语言表 t_tdm_dev_land_info_l

- **表名称：** 开发土地信息-多语言表
- **表名：** t_tdm_dev_land_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_dev_land_info_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_dev_land_info_l |  | fpkid |

---

## 土地信息详情登记-子表 t_tdm_dev_land_info_item

- **表名称：** 土地信息详情登记-子表
- **表名：** t_tdm_dev_land_info_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcqbck | 拆迁补偿款 | numeric | 23 | 10 | √ | 0 | 拆迁补偿款 |
| 3 | fqtzctz | 其他支出调整 | numeric | 23 | 10 | √ | 0 | 其他支出调整 |
| 4 | fitemmodifydate | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fyxdjtdjkhj | 允许抵减土地价款合计 | numeric | 23 | 10 | √ | 0 | 允许抵减土地价款合计 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fyxpjtdcrj | 有效票据土地出让金 | numeric | 23 | 10 | √ | 0 | 有效票据土地出让金 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fyxpjqqkffy | 有效票据前期开发费用 | numeric | 23 | 10 | √ | 0 | 有效票据前期开发费用 |
| 10 | fbgdjsq | 变更登记属期 | timestamp | 0 |  |  | null | 变更登记属期 |
| 11 | fdsjrzksmj | 地上计容总可售面积 | numeric | 23 | 10 | √ | 0 | 地上计容总可售面积 |
| 12 | fitemmodifier | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_dev_land_info_item_fk |  | fid |
| 2 | pk_tdm_dev_land_info_item |  | fentryid |

---

## 开发土地信息-主表 t_tdm_dev_land_info

- **表名称：** 开发土地信息-主表
- **表名：** t_tdm_dev_land_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcqbck | 拆迁补偿款 | numeric | 23 | 10 | √ | 0 | 拆迁补偿款 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fstage | 工程项目分期 | int8 | 64 |  | √ | 0 | [分期信息 bastax_stage](../bastax_files/bastax_stage.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fyxdjtdjkhj | 允许抵减土地价款合计 | numeric | 23 | 10 | √ | 0 | 允许抵减土地价款合计 |
| 8 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fyxpjqqkffy | 有效票据前期开发费用 | numeric | 23 | 10 | √ | 0 | 有效票据前期开发费用 |
| 10 | fdsjrzksmj | 地上计容总可售面积 | numeric | 23 | 10 | √ | 0 | 地上计容总可售面积 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fqtzctz | 其他支出调整 | numeric | 23 | 10 | √ | 0 | 其他支出调整 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fyxpjtdcrj | 有效票据土地出让金 | numeric | 23 | 10 | √ | 0 | 有效票据土地出让金 |
| 18 | fnumber | 土地信息编号 | varchar | 30 |  | √ | ' ' | 土地信息编号 |
| 19 | fproject | 税务项目 | int8 | 64 |  | √ | 0 | [税务项目信息 bastax_taxproject](../bastax_files/bastax_taxproject.md) |
| 20 | fdsjrzksmjtb | 地上计容总可售面积（同步房间信息） | numeric | 23 | 10 | √ | 0 | 地上计容总可售面积（同步房间信息） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_dev_land_info |  | fid |
| 2 | idx_t_tdm_dev_land_info_uniq1 |  | forgid,fproject,fstage |
