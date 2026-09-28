# 商品变更管理-ent_prodchange_manage

## 变更分录-子表 t_mal_prodchgentry

- **表名称：** 变更分录-子表
- **表名：** t_mal_prodchgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finfotype | 信息类型 | bpchar | 1 |  | √ | ' ' | 信息类型,枚举: S :字符 N :数值 D :日期 I :整数 B :布尔 Z :基础资料 A :附件 E :分录 P :图片 L :长文本 |
| 3 | foldvalue_tag | 变更前内容_详情 | text | 0 |  |  | null | 变更前内容_详情 |
| 4 | fsrcdata | 后台值 | varchar | 255 |  | √ | ' ' | 后台值 |
| 5 | ffieldname | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 6 | foldvalue | 变更前内容 | text | 0 |  |  | null | 变更前内容 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fentryseq | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 10 | fentryname | 分录实体标识 | varchar | 50 |  | √ | ' ' | 分录实体标识 |
| 11 | fchgfield | 变更字段 | varchar | 100 |  | √ | ' ' | 变更字段 |
| 12 | fsrcbillentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 13 | fnewvalue | 变更后内容 | text | 0 |  |  | null | 变更后内容 |
| 14 | fnewvalue_tag | 变更后内容_详情 | text | 0 |  |  | null | 变更后内容_详情 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodchgentry_fid_fseq |  | fid,fseq |
| 2 | pk_t_mal_prodchgentry |  | fentryid |

---

## 商品变更管理-多语言表 t_mal_prodchg_l

- **表名称：** 商品变更管理-多语言表
- **表名：** t_mal_prodchg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_prodchg_l_fid |  | fid,flocaleid |
| 2 | pk_t_mal_prodchg_l |  | fpkid |

---

## 商品变更管理-主表 t_mal_prodchg

- **表名称：** 商品变更管理-主表
- **表名：** t_mal_prodchg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 审批单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbilldate | 发起日期 | timestamp | 0 |  |  | null | 发起日期 |
| 4 | fprodid | 商品编码 | int8 | 64 |  | √ | 0 | [商品管理 ent_prodmanage](../ent_files/ent_prodmanage.md) |
| 5 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fattributedelete | 删除商品属性 | varchar | 255 |  | √ | ' ' | 删除商品属性 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 9 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | foldpicture4 | 商品图片5（变更前） | varchar | 255 |  | √ | ' ' | 商品图片5（变更前） |
| 13 | foldpicture3 | 商品图片4（变更前） | varchar | 255 |  | √ | ' ' | 商品图片4（变更前） |
| 14 | foldpicture2 | 商品图片3（变更前） | varchar | 255 |  | √ | ' ' | 商品图片3（变更前） |
| 15 | fthumbnail | 商品主图（变更后） | varchar | 255 |  | √ | ' ' | 商品主图（变更后） |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | foldtpicture1 | 商品图片2（变更前） | varchar | 255 |  | √ | ' ' | 商品图片2（变更前） |
| 18 | fpicture4 | 商品图片5（变更后） | varchar | 255 |  | √ | ' ' | 商品图片5（变更后） |
| 19 | fpicture3 | 商品图片4（变更后） | varchar | 255 |  | √ | ' ' | 商品图片4（变更后） |
| 20 | fpicture2 | 商品图片3（变更后） | varchar | 255 |  | √ | ' ' | 商品图片3（变更后） |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fpicture1 | 商品图片2（变更后） | varchar | 255 |  | √ | ' ' | 商品图片2（变更后） |
| 23 | fcfmopinion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | freason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 26 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 27 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 |
| 29 | fattributeupdate | 更新商品属性 | varchar | 255 |  | √ | ' ' | 更新商品属性 |
| 30 | fattributeadd | 新增商品属性 | varchar | 255 |  | √ | ' ' | 新增商品属性 |
| 31 | fnumber | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 32 | foldthumbnail | 商品主图（变更前） | varchar | 255 |  | √ | ' ' | 商品主图（变更前） |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_prodchg |  | fid |
| 2 | idx_mal_prodchg_fmasterid |  | fmasterid |
| 3 | idx_mal_prodchg_fprodid |  | fprodid |
