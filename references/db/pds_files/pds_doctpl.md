# 函件模板-pds_doctpl

## 采购部门-多选基础资料表 t_pds_doctplpurdept

- **表名称：** 采购部门-多选基础资料表
- **表名：** t_pds_doctplpurdept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_doctplpurdept_bid |  | fbasedataid |
| 2 | pk_pds_doctplpurdept |  | fpkid |
| 3 | idx_pds_doctplpurdept_fid |  | fid |

---

## 采购组织-多选基础资料表 t_pds_doctplpurorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_pds_doctplpurorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_doctplpurorg_fid |  | fid |
| 2 | idx_pds_doctplpurorg_bid |  | fbasedataid |
| 3 | pk_pds_doctplpurorg |  | fpkid |

---

## 采购组-多选基础资料表 t_pds_doctplpurgroup

- **表名称：** 采购组-多选基础资料表
- **表名：** t_pds_doctplpurgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购业务组(封存) bd_pmoperatorgroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_doctplpurgroup_fid |  | fid |
| 2 | pk_pds_doctplpurgroup |  | fpkid |
| 3 | idx_pds_doctplpurgroup_bid |  | fbasedataid |

---

## 函件模板-多语言表 t_pds_doctpl_l

- **表名称：** 函件模板-多语言表
- **表名：** t_pds_doctpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fname | 模板名称 | varchar | 300 |  | √ | ' ' | 模板名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_doctpl_l |  | fpkid |
| 2 | idx_pds_doctpl_fid |  | fid,flocaleid |

---

## 函件模板-主表 t_pds_doctpl

- **表名称：** 函件模板-主表
- **表名：** t_pds_doctpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 模板名称 | varchar | 300 |  | √ | ' ' | 模板名称 |
| 5 | fcategory | 品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 6 | ftemplatecode | 统一消息平台模板编码 | varchar | 50 |  | √ | ' ' | 统一消息平台模板编码 |
| 7 | fbiznodeid | 应用的业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fnodefields | 插入业务节点字段 | text | 0 |  |  | null | 插入业务节点字段,枚举: |
| 11 | fsrctypeid | 招标流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 12 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fletterstype | 函件类型 | bpchar | 1 |  | √ | ' ' | 函件类型,枚举: 1 :中标 2 :备选 3 :未中标 4 :邀请函 5 :培养 6 :不推荐 7 :利益澄清 9 :预中标 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcontent_tag | 函件内容_详情 | text | 0 |  |  | null | 函件内容_详情 |
| 19 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 模板编码 | varchar | 30 |  | √ | ' ' | 模板编码 |
| 21 | fcontent | 函件内容 | text | 0 |  |  | null | 函件内容 |
| 22 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 23 | fisdefault | 是否默认 | bpchar | 1 |  | √ | '0' | 是否默认 |
| 24 | fsendtypeid | 函件发送方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_doctpl |  | fid |
| 2 | idx_pds_doctpl_mid |  | fmasterid |
| 3 | idx_pds_doctpl_number |  | fnumber |
| 4 | idx_pds_doctpl_nodeid |  | fbiznodeid |
| 5 | idx_pds_doctpl_typeid |  | fsrctypeid |
