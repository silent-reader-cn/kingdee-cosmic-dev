# 盘点方案-im_invcountscheme

## 盘点表分单规则-子表 t_im_invcountsche_dim

- **表名称：** 盘点表分单规则-子表
- **表名：** t_im_invcountsche_dim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensioncomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fdimension | 分单依据 | varchar | 80 |  | √ | ' ' | 分单依据,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountsche_fid |  | fid |
| 2 | t_im_invcountsche_dim_pkey |  | fentryid |

---

## 盘点方案-多语言表 t_im_invcountscheme_l

- **表名称：** 盘点方案-多语言表
- **表名：** t_im_invcountscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountscheme_l_fid |  | fid,flocaleid |
| 2 | t_im_invcountscheme_l_pkey |  | fpkid |

---

## 排序规则设置-子表 t_im_countshcemesortrule

- **表名称：** 排序规则设置-子表
- **表名：** t_im_countshcemesortrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsortype | 排序方式 | varchar | 50 |  | √ | ' ' | 排序方式,枚举: asc :升序 desc :降序 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsortprop | 排序字段属性 | varchar | 50 |  | √ | ' ' | 排序字段属性,枚举: number :编码 name :名称 |
| 5 | fsortfield | 排序字段 | varchar | 50 |  | √ | ' ' | 排序字段,枚举: material :物料 warehouse :仓库 location :仓位 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_countshcemesortrule |  | fentryid |

---

## 仓库-多选基础资料表 t_im_invcountsche_whs

- **表名称：** 仓库-多选基础资料表
- **表名：** t_im_invcountsche_whs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_invcountsche_whs_pkey |  | fpkid |
| 2 | idx_im_invcountsch_whs |  | fid |

---

## 盘点方案-主表 t_im_invcountscheme

- **表名称：** 盘点方案-主表
- **表名：** t_im_invcountscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcounttype | 盘点方式 | varchar | 5 |  | √ | ' ' | 盘点方式,枚举: A :定期盘点 |
| 3 | ffreezeoutin | 冻结出入库 | bpchar | 1 |  | √ | '0' | 冻结出入库 |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcompletestatus | 盘点完成状态 | varchar | 30 |  | √ | 'B' | 盘点完成状态,枚举: A :未完成 B :已完成 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdynamicenddate | 动盘日期范围.结束 | timestamp | 0 |  |  | null | 动盘日期范围.结束 |
| 8 | fbackupcondition | 数据备份条件 | varchar | 30 |  | √ | 'invacc' | 数据备份条件,枚举: invacc :即时库存 enddateinvacc :截止日期库存 |
| 9 | fenddate | 截止日期 | timestamp | 0 |  |  | null | 截止日期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdynamicstartdate | 动盘日期范围.开始 | timestamp | 0 |  |  | null | 动盘日期范围.开始 |
| 12 | ffilterstring | 通用过滤控件文本 | varchar | 255 |  | √ | ' ' | 通用过滤控件文本 |
| 13 | faccessnode | 取数节点 | varchar | 10 |  | √ | 'start' | 取数节点,枚举: start :截止日期初始 end :截止日期结存 |
| 14 | fdefaultvalue | 盘点数量默认值设置 | varchar | 5 |  | √ | '0' | 盘点数量默认值设置,枚举: B :0 A :账存数量 |
| 15 | fcountzeroinv | 零库存参与盘点 | bpchar | 1 |  | √ | '0' | 零库存参与盘点 |
| 16 | fbillno | 方案编号 | varchar | 80 |  | √ | ' ' | 方案编号 |
| 17 | fisdynamiccount | 启用动盘 | bpchar | 1 |  | √ | '0' | 启用动盘 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | ffilterstring_tag | 通用过滤控件文本_详情 | text | 0 |  |  | null | 通用过滤控件文本_详情 |
| 20 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fbillcretype | fbillcretype | bpchar | 1 |  | √ | '0' |  |
| 26 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 27 | fenablecheck | 启用复盘 | bpchar | 1 |  | √ | '0' | 启用复盘 |
| 28 | fschemename | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 29 | fexcludeenddate | 排除补单 | bpchar | 1 |  | √ | '1' | 排除补单 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountscheme_billno |  | fbillno |
| 2 | t_im_invcountscheme_pkey |  | fid |

---

## 仓位-多选基础资料表 t_im_invcountsche_loc

- **表名称：** 仓位-多选基础资料表
- **表名：** t_im_invcountsche_loc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountsch_loc |  | fid |
| 2 | t_im_invcountsche_loc_pkey |  | fpkid |

---

## 动盘单据设置-子表 t_im_dynamiccounbillentry

- **表名称：** 动盘单据设置-子表
- **表名：** t_im_dynamiccounbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdynamicbill | 单据类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_dynamiccounbillentry |  | fentryid |

---

## 物料-多选基础资料表 t_im_invcountsche_mat

- **表名称：** 物料-多选基础资料表
- **表名：** t_im_invcountsche_mat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountsch_mat |  | fid |
| 2 | t_im_invcountsche_mat_pkey |  | fpkid |
