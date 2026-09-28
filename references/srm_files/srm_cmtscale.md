# 企业规模及生产能力-srm_cmtscale

## 主营产品分录-子表 t_srm_entrygoods

- **表名称：** 主营产品分录-子表
- **表名：** t_srm_entrygoods

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgoodsnumber | 产品编码 | varchar | 100 |  | √ | ' ' | 产品编码 |
| 3 | fgoodsmodel | 品牌/规格 | varchar | 100 |  | √ | ' ' | 品牌/规格 |
| 4 | fmonthlycapacity | 月产能 | varchar | 100 |  | √ | ' ' | 月产能 |
| 5 | fgoodsname | 产品名称 | varchar | 100 |  | √ | ' ' | 产品名称 |
| 6 | fyearcapacity | 年产能 | varchar | 100 |  | √ | ' ' | 年产能 |
| 7 | fcapacityuse | 可供我司月产能 | varchar | 100 |  | √ | ' ' | 可供我司月产能 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fgoodsdesc | 详细描述 | varchar | 255 |  | √ | ' ' | 详细描述 |
| 10 | fproduct | 供我司产品 | varchar | 255 |  | √ | ' ' | 供我司产品 |
| 11 | fgoodsnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_entrygoods |  | fentryid |
| 2 | idx_srm_entrygoods_fid |  | fid |

---

## 企业规模及生产能力-主表 t_srm_compentscale

- **表名称：** 企业规模及生产能力-主表
- **表名：** t_srm_compentscale

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flownum | 最小量 | int8 | 64 |  | √ | 0 | 最小量 |
| 3 | fmanagementstaff | 管理人员数 | int8 | 64 |  | √ | 0 | 管理人员数 |
| 4 | ftwoyearlaterquo | 2年以上质量人员占比 (%) | int8 | 64 |  | √ | 0 | 2年以上质量人员占比 (%) |
| 5 | foutproductday | 接单→出货 (天) | int8 | 64 |  | √ | 0 | 接单→出货 (天) |
| 6 | fpentitykey | 父单据标识 | varchar | 100 |  | √ | ' ' | 父单据标识 |
| 7 | fislow | 是否有最小生产批量/最低订货要求 | varchar | 10 |  | √ | ' ' | 是否有最小生产批量/最低订货要求,枚举: 1 :是 2 :否 |
| 8 | fengineernum | 工程技术人员 | int8 | 64 |  | √ | 0 | 工程技术人员 |
| 9 | fselfcheckpeo | 来料质检人数 | int8 | 64 |  | √ | 0 | 来料质检人数 |
| 10 | frdpeoplenum | 产品开发人员 | int8 | 64 |  | √ | 0 | 产品开发人员 |
| 11 | fqualitystaffnum | 质量人员数 | int8 | 64 |  | √ | 0 | 质量人员数 |
| 12 | fstaffnum | 企业规模数 | int8 | 64 |  | √ | 0 | 企业规模数 |
| 13 | fwarehousearea | 库房面积 (平米) | int8 | 64 |  | √ | 0 | 库房面积 (平米) |
| 14 | fofficearea | 办公室面积 (平米) | int8 | 64 |  | √ | 0 | 办公室面积 (平米) |
| 15 | ftechniciannum | 技术人员数 | int8 | 64 |  | √ | 0 | 技术人员数 |
| 16 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 17 | fparentid | 父单据ID | varchar | 100 |  | √ | ' ' | 父单据ID |
| 18 | fplantarea | 厂房面积 (平米) | int8 | 64 |  | √ | 0 | 厂房面积 (平米) |
| 19 | ftwoyearlater | 2年以上技术人员占比 (%) | int8 | 64 |  | √ | 0 | 2年以上技术人员占比 (%) |
| 20 | fproductsample | 样品生产周期 (天) | int8 | 64 |  | √ | 0 | 样品生产周期 (天) |
| 21 | fentitykey | 组件标识 | varchar | 100 |  | √ | ' ' | 组件标识 |
| 22 | fiqpcpeo | 制程质检人数 | int8 | 64 |  | √ | 0 | 制程质检人数 |
| 23 | fmainorgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | fproductday | 生产前置期 (天) | int8 | 64 |  | √ | 0 | 生产前置期 (天) |
| 25 | ffinshpropeo | 成品质检人数 | int8 | 64 |  | √ | 0 | 成品质检人数 |
| 26 | frdability | 研发能力 | varchar | 10 |  | √ | ' ' | 研发能力,枚举: A :能自主设计开发新产品 B :联合开发 C :委托开发 D :无开发能力 |
| 27 | ftotalpeople | 总人数 | int8 | 64 |  | √ | 0 | 总人数 |
| 28 | fisout | 产品/关键部件有无外发生产？ | varchar | 10 |  | √ | ' ' | 产品/关键部件有无外发生产？,枚举: 1 :是 2 :否 |
| 29 | ftransportday | 运输时间 (最远 天) | int8 | 64 |  | √ | 0 | 运输时间 (最远 天) |
| 30 | fannualsales | 年销售额 (万元) | int8 | 64 |  | √ | 0 | 年销售额 (万元) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_compentscale_parent |  | fparentid |
| 2 | pk_t_srm_compentscale |  | fid |

---

## 主要原材料情况-子表 t_srm_commainproduct

- **表名称：** 主要原材料情况-子表
- **表名：** t_srm_commainproduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fmaiproductname | 材料名称 | varchar | 255 |  | √ | ' ' | 材料名称 |
| 4 | fmaiproductsup | 供应商名称 | varchar | 255 |  | √ | ' ' | 供应商名称 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmainnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_commainproduct |  | fentryid |
| 2 | idx_srm_mainproduc_fid |  | fid |

---

## 协力厂商分录-子表 t_srm_compartnerentry

- **表名称：** 协力厂商分录-子表
- **表名：** t_srm_compartnerentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpartneraddress | 地址 | varchar | 100 |  | √ | ' ' | 地址 |
| 3 | fpartnername | 协力厂商 | varchar | 100 |  | √ | ' ' | 协力厂商 |
| 4 | fpartnerpho | 联系电话 | varchar | 100 |  | √ | ' ' | 联系电话 |
| 5 | fpartnerlink | 联系人 | varchar | 100 |  | √ | ' ' | 联系人 |
| 6 | fpartnerdate | 合作时间 | varchar | 100 |  | √ | ' ' | 合作时间 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | frelation | 合作关系 | varchar | 10 |  | √ | ' ' | 合作关系,枚举: A :控股 B :投资入股 C :长期合作 D :短期合作 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fpartnergoods | 协力产品 | varchar | 100 |  | √ | ' ' | 协力产品 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_cpartnerentry_fid |  | fid |
| 2 | pk_t_srm_compartnerentry |  | fentryid |

---

## 主要生产设配情况-子表 t_srm_comproductentry

- **表名称：** 主要生产设配情况-子表
- **表名：** t_srm_comproductentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductoolname | 生产设备名称与型号 | varchar | 255 |  | √ | ' ' | 生产设备名称与型号 |
| 3 | fproduction | 生产设配厂商 | varchar | 255 |  | √ | ' ' | 生产设配厂商 |
| 4 | fdate | 购入日期 | timestamp | 0 |  |  | null | 购入日期 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fability | 单机产能 | varchar | 100 |  | √ | ' ' | 单机产能 |
| 8 | fproductoolnum | 设备数量 | int8 | 64 |  | √ | 0 | 设备数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_cproductentry_fid |  | fid |
| 2 | pk_t_srm_comproductentry |  | fentryid |
