# 引入方案详情-iptm_scheme

## 目标业务对象-多选基础资料表 t_iptm_multarmeta

- **表名称：** 目标业务对象-多选基础资料表
- **表名：** t_iptm_multarmeta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 目标业务对象列表 iptm_importtarget |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_multarmeta |  | fpkid |
| 2 | idx_t_iptm_multarmeta_id |  | fid |

---

## 字段映射-子表 t_iptm_schemefieldmapping

- **表名称：** 字段映射-子表
- **表名：** t_iptm_schemefieldmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffieldnumber | 字段编码 | varchar | 50 |  | √ | ' ' | 字段编码 |
| 2 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录,枚举: 1 :必录 |
| 3 | ffieldname | 字段名称 | varchar | 250 |  | √ | ' ' | 字段名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fstdpartname | 实体字段分组 | varchar | 250 |  | √ | ' ' | 实体字段分组 |
| 8 | ftextfield | 文档内字段 | varchar | 250 |  | √ | ' ' | 文档内字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_schemefieldmapping |  | fdetailid |
| 2 | idx_t_iptm_sfmapping_entryid |  | fentryid |

---

## 引入方案详情-多语言表 t_iptm_scheme_l

- **表名称：** 引入方案详情-多语言表
- **表名：** t_iptm_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_scheme_l |  | fpkid |
| 2 | idx_iptm_scheme_l_localeid |  | fid,flocaleid |

---

## 引入任务分录-子表 t_iptm_schemedetail

- **表名称：** 引入任务分录-子表
- **表名：** t_iptm_schemedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freplacekeyword | freplacekeyword | varchar | 50 |  | √ | ' ' |  |
| 3 | frelpropname | 多Sheet页关联识别的唯一值 | varchar | 50 |  | √ | ' ' | 多Sheet页关联识别的唯一值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | freplacekeyfield | 数据替换规则的唯一值 | varchar | 50 |  | √ | ' ' | 数据替换规则的唯一值 |
| 6 | fbillentity | 业务对象标识 | varchar | 36 |  | √ | ' ' | 目标业务对象列表 iptm_importtarget |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsourcesheet | 指定 Sheet 页签 | varchar | 100 |  | √ | ' ' | 指定 Sheet 页签 |
| 9 | fimporttype | 指定引入方式 | varchar | 50 |  | √ | ' ' | 指定引入方式,枚举: new :添加新数据 override :更新已有数据 overridenew :更新已有数据并添加新数据 |
| 10 | fcolumnmapping | fcolumnmapping | varchar | 50 |  | √ | ' ' |  |
| 11 | fdependency | fdependency | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iptm_schemedetail_fid |  | fid |
| 2 | pk_t_iptm_schemedetail |  | fentryid |

---

## 引入方案详情-主表 t_iptm_scheme

- **表名称：** 引入方案详情-主表
- **表名：** t_iptm_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodelinfo | 模板信息 | varchar | 255 |  | √ | ' ' | 模板信息 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fshared | 共享状态 | varchar | 50 |  | √ | ' ' | 共享状态,枚举: 0 :私有 1 :共享 |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreateorg | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmodelinfo_tag | 模板信息_详情 | text | 0 |  |  | null | 模板信息_详情 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 18 | fdesc | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_iptm_scheme_fnumber |  | fnumber |
| 2 | pk_t_iptm_scheme |  | fid |
