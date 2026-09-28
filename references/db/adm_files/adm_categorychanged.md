# 品类库变更-adm_categorychanged

## 品类分录-子表 t_pur_categorychgentry

- **表名称：** 品类分录-子表
- **表名：** t_pur_categorychgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupcategoryid | 供应商品类库 | int8 | 64 |  | √ | 0 | [供应商品类库 srm_supcategory](../srm_files/srm_supcategory.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 6 | fissourcelist | 更新货源清单 | bpchar | 1 |  | √ | '0' | 更新货源清单 |
| 7 | fcategorytype | 类型 | bpchar | 1 |  | √ | 'B' | 类型,枚举: A :物料 B :品类 |
| 8 | fcategorystatus | 变更后状态 | bpchar | 1 |  | √ | ' ' | 变更后状态,枚举: 1 :有效 2 :无效 3 :冻结 |
| 9 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | fcategoryid | 采购品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 11 | fmaterial | 物料名称 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcategorystatus_old | 当前品类状态 | bpchar | 1 |  | √ | ' ' | 当前品类状态,枚举: 1 :有效 2 :无效 3 :冻结 4 :退出 5 :新增 9 :未引入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_categorychg_fid_fseq |  | fid,fseq |
| 2 | t_pur_categorychgentry_pkey |  | fentryid |

---

## 品类库变更-主表 t_pur_categorychg

- **表名称：** 品类库变更-主表
- **表名：** t_pur_categorychg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 变更说明 | varchar | 255 |  | √ | ' ' | 变更说明 |
| 3 | finitiator | 发起方 | bpchar | 1 |  | √ | '0' | 发起方,枚举: 0 :采购方 1 :供应商 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 10 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 |
| 12 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 13 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 14 | forgstatus | forgstatus | bpchar | 1 |  | √ | ' ' |  |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_categorychg_pkey |  | fid |
| 2 | idx_pur_categorychg_fbillno |  | fbillno |
| 3 | idx_pur_categorychg_fbilldate |  | fbilldate |

---

## 品类库变更-多语言表 t_pur_categorychg_l

- **表名称：** 品类库变更-多语言表
- **表名：** t_pur_categorychg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 变更说明 | varchar | 255 |  | √ | ' ' | 变更说明 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_categorychg_l_pkey |  | fpkid |
| 2 | idx_pur_categorychg_l_fid |  | fid,flocaleid |

---

## 品类库变更-分表 t_pur_categorychg_a

- **表名称：** 品类库变更-分表
- **表名：** t_pur_categorychg_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fcfmdate | fcfmdate | timestamp | 0 |  |  | null |  |
| 8 | fauditopinion | fauditopinion | varchar | 255 |  | √ | ' ' |  |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fcfmid | fcfmid | int8 | 64 |  | √ | 0 |  |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_categorychg_a_pkey |  | fid |
| 2 | idx_pur_categorychg_a_ftime |  | fcreatetime |
