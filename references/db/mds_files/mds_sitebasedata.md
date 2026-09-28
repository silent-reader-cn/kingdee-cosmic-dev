# 供应组织分配供应定义-mds_sitebasedata

## 生产事务类型-多选基础资料表 t_mds_sitetranproduct

- **表名称：** 生产事务类型-多选基础资料表
- **表名：** t_mds_sitetranproduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 生产事务类型 mpdm_transactproduct |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_sitetranproduct |  | fpkid |
| 2 | idx_y_mds_sitetranproduct |  | fid,fbasedataid |

---

## 仓库设置-子表 t_mds_sitebaseset

- **表名称：** 仓库设置-子表
- **表名：** t_mds_sitebaseset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpriority | fpriority | int8 | 64 |  | √ | 0 |  |
| 3 | fstocknumberid | 仓库编码 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fiswastewh | fiswastewh | bpchar | 1 |  | √ | '0' |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fstockorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fstockindexid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_sitebaseset |  | fentryid |
| 2 | idx_y_mds_sitebaseset |  | fid |

---

## 供应优先级-子表 t_mds_sitebaseentry

- **表名称：** 供应优先级-子表
- **表名：** t_mds_sitebaseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplytype | 供应类型 | varchar | 50 |  | √ | ' ' | 供应类型,枚举: A :库存 B :生产工单 C :日生产计划 D :SOP |
| 3 | fsupptype | fsupptype | varchar | 50 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fisselected | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_y_mds_sitebaseentry |  | fid |
| 2 | pk_t_mds_sitebaseentry |  | fentryid |

---

## 库存类型-子表 t_mds_sitebasetype

- **表名称：** 库存类型-子表
- **表名：** t_mds_sitebasetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismrp | 参与供应组织分配计算 | bpchar | 1 |  | √ | '1' | 参与供应组织分配计算 |
| 3 | fstocktypeid | 编码 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_sitebasetype |  | fentryid |
| 2 | idx_y_mds_sitebasetype |  | fid |

---

## 库存状态-子表 t_mds_sitebasestatus

- **表名称：** 库存状态-子表
- **表名：** t_mds_sitebasestatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fismrp | 参与供应组织分配计算 | bpchar | 1 |  | √ | '1' | 参与供应组织分配计算 |
| 3 | fstocktypeid | 编码 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_sitebasestatus |  | fentryid |
| 2 | idx_y_mds_sitebasestatus |  | fid |

---

## 供应组织分配供应定义-多语言表 t_mds_sitebasedata_l

- **表名称：** 供应组织分配供应定义-多语言表
- **表名：** t_mds_sitebasedata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_sitebasedata_l |  | fpkid |
| 2 | idx_y_mds_sitebasedata_l |  | fid,flocaleid |

---

## 日生产计划版本-多选基础资料表 t_mds_sitedpsversion

- **表名称：** 日生产计划版本-多选基础资料表
- **表名：** t_mds_sitedpsversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_sitedpsversion |  | fpkid |
| 2 | idx_y_mds_sitedpsversion |  | fid,fbasedataid |

---

## 供应组织分配供应定义-主表 t_mds_sitebasedata

- **表名称：** 供应组织分配供应定义-主表
- **表名：** t_mds_sitebasedata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fstocksetup | 单选按钮组 | varchar | 50 |  | √ | ' ' | 单选按钮组,枚举: 1 :全部仓库 3 :不参与供应组织分配计算仓库 2 :参与供应组织分配计算仓库 |
| 5 | fsopversionid | fsopversionid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fdpsversionid | fdpsversionid | int8 | 64 |  | √ | 0 |  |
| 11 | ftransactproductid | ftransactproductid | int8 | 64 |  | √ | 0 |  |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fbillstatuscheckbox | 日生产计划确认状态 | bpchar | 1 |  | √ | '0' | 日生产计划确认状态 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_sitebasedata |  | fid |
| 2 | idx_num_mds_sitebasedata |  | fnumber |
