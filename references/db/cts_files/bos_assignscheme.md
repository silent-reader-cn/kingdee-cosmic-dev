# 方案分配列表-bos_assignscheme

## 方案分配列表-多语言表 t_cts_layoutschemeassign_l

- **表名称：** 方案分配列表-多语言表
- **表名：** t_cts_layoutschemeassign_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_layoutassign_l_id |  | fid,flocaleid |
| 2 | pk_t_cts_layoutschemeassign_l |  | fpkid |

---

## 方案分配列表-主表 t_cts_layoutschemeassign

- **表名称：** 方案分配列表-主表
- **表名：** t_cts_layoutschemeassign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fincludesuborg | 包含下级组织 | bpchar | 1 |  | √ | '0' | 包含下级组织,枚举: 1 :是 0 :否 |
| 5 | fappid | 所属应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 6 | flayoutschemeid | 界面方案 | int8 | 64 |  | √ | 0 | 界面个性化配置 bos_newpageconfig |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatedate | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 9 | ftype | 分配类型 | bpchar | 1 |  | √ | ' ' | 分配类型,枚举: 1 :组织分配 2 :单据类型分配 3 :单据类型+组织分配 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fcloudid | 所属云 | varchar | 36 |  | √ | ' ' | 业务云 bos_devportal_bizcloud |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 36 |  | √ | ' ' | 编码 |
| 16 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_layoutassign_orgid |  | forgid |
| 2 | idx_cts_layoutassign_btid |  | fbilltypeid |
| 3 | idx_cts_layoutassign_schemeid |  | flayoutschemeid |
| 4 | pk_t_cts_layoutschemeassign |  | fid |
