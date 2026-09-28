# 人员可销范围-ocdbd_memberscopes

## 人员可销范围-主表 t_ocdbd_salescope

- **表名称：** 人员可销范围-主表
- **表名：** t_ocdbd_salescope

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcontroltype | 控制类型 | bpchar | 1 |  | √ | 'A' | 控制类型,枚举: A :允许销售 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsalestargettype | 可销对象类型 | bpchar | 1 |  | √ | 'A' | 可销对象类型,枚举: A :人员 B :商务伙伴用户 C :部门 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fsalesscope | 可销范围 | bpchar | 1 |  | √ | 'A' | 可销范围,枚举: A :商品 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbizorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_salescope_number |  | fnumber |
| 2 | pk_ocdbd_salescope |  | fid |

---

## 可销对象单据体-子表 t_ocdbd_salescopeuser

- **表名称：** 可销对象单据体-子表
- **表名：** t_ocdbd_salescopeuser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpartnerid | fpartnerid | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fuserid | 人员编码 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbizpartnerid | 商务伙伴用户 | int8 | 64 |  | √ | 0 | 商务伙伴用户 bos_bizpartneruser |
| 6 | fusername | 伙伴用户名称 | varchar | 80 |  | √ | ' ' | 伙伴用户名称 |
| 7 | fusernumber | 伙伴用户手机号 | varchar | 80 |  | √ | ' ' | 伙伴用户手机号 |
| 8 | fchannelid | 所属渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 9 | fusertypeid | fusertypeid | int8 | 64 |  | √ | 0 |  |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | forganizationid | 行政组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fissaler | 是否销售员 | bpchar | 1 |  | √ | '1' | 是否销售员 |
| 13 | ftargettype | 对象类型 | bpchar | 1 |  | √ | 'A' | 对象类型,枚举: A :人员 B :商务伙伴用户 C :部门 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_salescopeuser_fid |  | fid |
| 2 | pk_ocdbd_salescopeuser |  | fentryid |

---

## 商品明细单据体-子表 t_ocdbd_salescopeitem

- **表名称：** 商品明细单据体-子表
- **表名：** t_ocdbd_salescopeitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbrandid | 商品品牌 | int8 | 64 |  | √ | 0 | 商品品牌 mdr_item_brand |
| 2 | fitemlabelid | 商品标签 | int8 | 64 |  | √ | 0 | 商品标签 ocdbd_item_label |
| 3 | ftype | 类型 | bpchar | 1 |  | √ | '1' | 类型,枚举: 1 :商品 2 :商品分类 3 :商品品牌 4 :商品标签 |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 5 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_salescopeitem |  | fdetailid |
| 2 | idx_ocdbd_salescopeitem_eid |  | fentryid |

---

## 人员可销范围-多语言表 t_ocdbd_salescope_l

- **表名称：** 人员可销范围-多语言表
- **表名：** t_ocdbd_salescope_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_salescope_l |  | fpkid |
| 2 | idx_ocdbd_salescope_fidlid |  | fid,flocaleid |
