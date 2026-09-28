# 授信申请-creditm_apply

## 组织共享分录-子表 t_creditm_apply_org

- **表名称：** 组织共享分录-子表
- **表名：** t_creditm_apply_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalamt | 分配额度 | numeric | 19 | 6 | √ | 0 | 分配额度 |
| 3 | fsingleamt | 限定额度 | numeric | 19 | 6 | √ | 0 | 限定额度 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | foldsingleamt | 调整前额度 | numeric | 19 | 6 | √ | 0 | 调整前额度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_crapply_org_fid |  | fid |
| 2 | pk_t_creditm_apply_org |  | fentryid |

---

## 授信申请-主表 t_creditm_apply

- **表名称：** 授信申请-主表
- **表名：** t_creditm_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fcredittypeid | 授信类别 | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 4 | fcreditprop | 授信性质 | varchar | 30 |  | √ | ' ' | 授信性质,枚举: circle :循环 fix :非循环 |
| 5 | frenewalenddate | 续期后到期日期 | timestamp | 0 |  |  | null | 续期后到期日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fenddate | 授信结束日期 | timestamp | 0 |  |  | null | 授信结束日期 |
| 8 | fcreatorid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fapplytype | 申请类型 | varchar | 30 |  | √ | ' ' | 申请类型,枚举: add :新增申请 join :加入申请 renewal :续期申请 adjust :调整申请 |
| 10 | fisgrouplimit | 是否集团授信 | bpchar | 1 |  | √ | '0' | 是否集团授信 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fbanktype | 授信机构类别 | varchar | 30 |  | √ | 'bd_finorginfo' | 授信机构类别,枚举: bd_finorginfo :机构授信 bos_org :内部授信 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 16 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fguartype | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证 ensuamt :保证金 mortgage :抵押 pledge :质押 credit :信用 other :其他 |
| 19 | fishascreditlimit | 是否生成额度单 | bpchar | 1 |  | √ | '0' | 是否生成额度单 |
| 20 | fguaranteeorgid | 担保组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fcontractno | 授信协议号 | varchar | 80 |  | √ | ' ' | 授信协议号 |
| 23 | ftotalamt | 申请总额 | numeric | 19 | 6 | √ | 0 | 申请总额 |
| 24 | fstartdate | 授信开始日期 | timestamp | 0 |  |  | null | 授信开始日期 |
| 25 | forgsharetype | 组织共享方式 | varchar | 30 |  | √ | ' ' | 组织共享方式,枚举: downshare :向下共享 appointshare :指定共享 |
| 26 | fbankid | 授信机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 27 | fcurrencyid | 授信币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fcreditlimitid | 选择额度单 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_creditm_apply_org |  | forgid |
| 2 | pk_t_creditm_apply |  | fid |
| 3 | idx_t_creditm_apply_status |  | fbillstatus |
| 4 | idx_t_creditm_apply_billno |  | fbillno |

---

## 授信类别-多选基础资料表 t_creditm_apply_type_m

- **表名称：** 授信类别-多选基础资料表
- **表名：** t_creditm_apply_type_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_crapply_typem_id |  | fentryid |
| 2 | pk_t_creditm_apply_type_m |  | fpkid |

---

## 授信申请-多语言表 t_creditm_apply_l

- **表名称：** 授信申请-多语言表
- **表名：** t_creditm_apply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 80 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_creditm_apply_l |  | fpkid |
| 2 | idx_t_crapply_l_fid |  | fid,flocaleid |

---

## 类别共享分录-子表 t_creditm_apply_type

- **表名称：** 类别共享分录-子表
- **表名：** t_creditm_apply_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalamt | 分配额度 | numeric | 19 | 6 | √ | 0 | 分配额度 |
| 3 | fsingleamt | 限定额度 | numeric | 19 | 6 | √ | 0 | 限定额度 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_crapply_type_fid |  | fid |
| 2 | pk_t_creditm_apply_type |  | fentryid |

---

## 资金组织-多选基础资料表 t_creditm_apply_org_m

- **表名称：** 资金组织-多选基础资料表
- **表名：** t_creditm_apply_org_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_creditm_apply_org_m |  | fpkid |
| 2 | idx_t_crapply_orgm_id |  | fentryid |
