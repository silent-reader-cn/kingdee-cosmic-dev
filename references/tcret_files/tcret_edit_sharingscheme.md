# 房产租金共享方案-tcret_edit_sharingscheme

## 规则-子表 t_tcret_sharingschemerule

- **表名称：** 规则-子表
- **表名：** t_tcret_sharingschemerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: income :收入规则 rollout :进项转出规则 diff :差额扣除规则 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_sharingschemerule_fk |  | fentryid |
| 2 | pk_tcret_sharingschemerule |  | fdetailid |

---

## 共享方案-子表 t_tcret_sharingscheme

- **表名称：** 共享方案-子表
- **表名：** t_tcret_sharingscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 10 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 11 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbasedatapropfield | fbasedatapropfield | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_sharingscheme |  | fentryid |
| 2 | idx_tcret_sharingscheme_fid |  | fid |

---

## 被共享组织-子表 t_tcret_sharingscheme_org

- **表名称：** 被共享组织-子表
- **表名：** t_tcret_sharingscheme_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_sharingscheme_org |  | fdetailid |
| 2 | idx_tcret_sharingscheme_org_fk |  | fentryid |

---

## 适用租赁项目-子表 t_tcret_sharingscheme_lea

- **表名称：** 适用租赁项目-子表
- **表名：** t_tcret_sharingscheme_lea

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fleaseid | 租赁项目 | int8 | 64 |  | √ | 0 | 房产出租信息 tdm_house_rental_info |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_sharingscheme_lea_fk |  | fentryid |
| 2 | idx_sharingscheme_lea_fleaseid |  | fleaseid |
| 3 | pk_tcret_sharingscheme_lea |  | fdetailid |

---

## 共享方案-多语言表 t_tcret_sharingscheme_l

- **表名称：** 共享方案-多语言表
- **表名：** t_tcret_sharingscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 共享方案名 | varchar | 50 |  | √ | ' ' | 共享方案名 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_sharingscheme_l_0 |  | fentryid,flocaleid |
| 2 | pk_tcret_sharingscheme_l |  | fpkid |

---

## 房产租金共享方案-主表 t_tcret_editsharingscheme

- **表名称：** 房产租金共享方案-主表
- **表名：** t_tcret_editsharingscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fautoshar | 自动共享 | bpchar | 1 |  | √ | ' ' | 自动共享 |
| 4 | fplanname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_editsharingscheme_forgid |  | forgid |
| 2 | pk_tcret_editsharingscheme |  | fid |
