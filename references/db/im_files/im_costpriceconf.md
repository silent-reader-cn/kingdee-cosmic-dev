# 获取成本配置-im_costpriceconf

## 成本回填字段映射-子表 t_im_costcolsmapentry

- **表名称：** 成本回填字段映射-子表
- **表名：** t_im_costcolsmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostrecordfieldkey | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 3 | fimbillfieldkey | 标识 | varchar | 100 |  | √ | ' ' | 标识 |
| 4 | fcostrecordfield | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fimbillfield | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_costcolsmapentry |  | fentryid |
| 2 | idx_im_colsmapentry_eid |  | fid |

---

## 获取成本配置-主表 t_im_costpriceconf

- **表名称：** 获取成本配置-主表
- **表名：** t_im_costpriceconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillentry | 单据体 | varchar | 50 |  | √ | ' ' | 单据体 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fimbill | 库存单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fbillentrykey | 单据体标识 | varchar | 50 |  | √ | ' ' | 单据体标识 |
| 8 | foperationname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 9 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 10 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcostaccount | 成本账簿 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | ffilterjson | 数据范围json | varchar | 255 |  | √ | ' ' | 数据范围json |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | faccounttype | 账簿类别 | int8 | 64 |  | √ | 0 | [成本主体类别 cal_bd_costaccounttype](../cal_files/cal_bd_costaccounttype.md) |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | ffilterformula_tag | 数据范围表达式_详情 | text | 0 |  |  | null | 数据范围表达式_详情 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | fiscostmainaccount | 成本主账簿 | bpchar | 1 |  | √ | '0' | 成本主账簿 |
| 22 | foperation | 调用服务的操作 | varchar | 50 |  | √ | ' ' | 调用服务的操作,枚举: |
| 23 | ffilterjson_tag | 数据范围json_详情 | text | 0 |  |  | null | 数据范围json_详情 |
| 24 | ffilterformula | 数据范围表达式 | varchar | 255 |  | √ | ' ' | 数据范围表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_costpriceconf |  | fid |
| 2 | idx_im_costpriceconf_num |  | fnumber |

---

## 获取成本配置-多语言表 t_im_costpriceconf_l

- **表名称：** 获取成本配置-多语言表
- **表名：** t_im_costpriceconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | foperationname | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_costpriceconf_l |  | fpkid |
| 2 | idx_im_costpriceconf_l_id |  | fid,flocaleid |
