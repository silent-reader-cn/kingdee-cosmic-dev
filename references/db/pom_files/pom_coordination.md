# 跨行业协调单-pom_coordination

## 图纸附件-附件表 t_pom_drawattachment

- **表名称：** 图纸附件-附件表
- **表名：** t_pom_drawattachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_drawattachment |  | fpkid |
| 2 | idx_t_pom_drawattachment |  | fid |

---

## 关联子实体-子表 t_sfc_coordination_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_coordination_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_coordination_lk |  | fpkid |
| 2 | idx_sfc_coordination_lk_fk |  | fid |

---

## 热处理-子表 t_pom_coordina_heat

- **表名称：** 热处理-子表
- **表名：** t_pom_coordina_heat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funitheat | 计量单位（热处理） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | fqtyheat | 数量（热处理） | numeric | 23 | 10 | √ | 0 | 数量（热处理） |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fmaterialheat | 零件号（热处理） | int8 | 64 |  | √ | 0 | 物料 bd_material |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_coordina_heat_fk |  | fid |
| 2 | pk_pom_coordina_heat |  | fentryid |

---

## 单据体-子表 t_pom_surface

- **表名称：** 单据体-子表
- **表名：** t_pom_surface

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsurfacemunit | 计量单位（表面处理） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | fsurfacemqty | 数量（表面处理） | numeric | 23 | 10 | √ | 0 | 数量（表面处理） |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fsurfacemno | 零件号（表面处理） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fsurfacetype | 表面处理类型 | varchar | 50 |  | √ | ' ' | 表面处理类型,枚举: A :Cadmium Plating 镉电镀 B :Passivation 钝化 C :Anodizing 阳极氧化 D :Stylus Cadmium Plating 刷镀镉 E :Bonderite M-CR 600 Aero F :Bonderite M-CR 1200S Aero G :Bonderite M-CR 1500 Aero |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_surface |  | fentryid |
| 2 | idx_pom_surface_fk |  | fid |

---

## 机械加工-子表 t_pom_coordina_mac

- **表名称：** 机械加工-子表
- **表名：** t_pom_coordina_mac

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funitmac | 计量单位（机械加工） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | fmaterialmac | 零件号（机械加工） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | fqtymac | 数量（机械加工） | numeric | 23 | 10 | √ | 0 | 数量（机械加工） |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_coordina_mac_fk |  | fid |
| 2 | pk_pom_coordina_mac |  | fentryid |

---

## 跨行业协调单-关联追踪表 t_sfc_coordination_tc

- **表名称：** 跨行业协调单-关联追踪表
- **表名：** t_sfc_coordination_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_coordination_tc |  | fid |
| 2 | idx_sfc_coordination_tc_tbill |  | ftbillid |
| 3 | idx_sfc_coordination_tc_tid |  | ftid |

---

## 跨行业协调单-反写记录表 t_sfc_coordination_wb

- **表名称：** 跨行业协调单-反写记录表
- **表名：** t_sfc_coordination_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_coordination_wb_fk |  | fid |
| 2 | pk_sfc_coordination_wb |  | fentryid |

---

## 跨行业协调单-主表 t_pom_coordination

- **表名称：** 跨行业协调单-主表
- **表名：** t_pom_coordination

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproviddate | 提供日期 | timestamp | 0 |  |  | null | 提供日期 |
| 3 | frawmaterialname | 原材料名称（废弃） | varchar | 50 |  | √ | ' ' | 原材料名称（废弃） |
| 4 | fspraypartdowntype1 | fspraypartdowntype1 | varchar | 50 |  | √ | ' ' |  |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | frecipitrade | 接收者行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 7 | fspraypartface | 面漆 | bpchar | 1 |  | √ | '0' | 面漆 |
| 8 | fapplytrade | 申请者行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |
| 9 | fworkstartdate | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 10 | fpickdate | 取走日期 | timestamp | 0 |  |  | null | 取走日期 |
| 11 | fworkremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fheatpartno | 零件号（封存） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 14 | fjobno | 检修工单号（废弃） | varchar | 50 |  | √ | ' ' | 检修工单号（废弃） |
| 15 | fheatpartqty | 数量（封存） | numeric | 23 | 10 | √ | 0 | 数量（封存） |
| 16 | fenddate | 期望完成时间 | timestamp | 0 |  |  | null | 期望完成时间 |
| 17 | fisairproject | 是否飞机项目 | bpchar | 1 |  | √ | '0' | 是否飞机项目 |
| 18 | fsparymaterial | 部件零件号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 19 | fprojectno | 项目号 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 20 | fworkpress | 紧急 | bpchar | 1 |  | √ | '0' | 紧急 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | frequirefinalstatus | 要求热处理到最终状态 | varchar | 255 |  | √ | ' ' | 要求热处理到最终状态 |
| 23 | fheatpartunit | 计量单位（封存） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fdocument | 参考文件 | varchar | 50 |  | √ | ' ' | 参考文件 |
| 25 | fspraypartqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fmaterialno | 原材料编号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 27 | fspraypartdoc | 参考文件 | varchar | 50 |  | √ | ' ' | 参考文件 |
| 28 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fpicker | 取走者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fmratype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 31 | fspraypartunit | 计量单位（零件喷漆） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 32 | fpreenddate | 预计完成时间 | timestamp | 0 |  |  | null | 预计完成时间 |
| 33 | fissparymaterail | 是否喷零件号 | bpchar | 1 |  | √ | '0' | 是否喷零件号 |
| 34 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 35 | fworkteam | 工作组 | varchar | 50 |  | √ | ' ' | 工作组,枚举: A :木工组 |
| 36 | fmachiningunit | 计量单位（封存） | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fmaterielmtc | 检修设备注册号 | int8 | 64 |  | √ | 0 | 物料检修信息 mpdm_materialmtcinfo |
| 38 | fmachiningdoc | 要求机械加工的文件 | varchar | 50 |  | √ | ' ' | 要求机械加工的文件,枚举: A :附件工卡SWS B :图纸 C :TAR D :其它 |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | fmachiningqty | 数量（封存） | numeric | 23 | 10 | √ | 0 | 数量（封存） |
| 41 | fairregistno | 检修设备注册号（废弃） | varchar | 50 |  | √ | ' ' | 检修设备注册号（废弃） |
| 42 | fprovider | 提供者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fmachnipartno | 零件号（封存） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 44 | fairtype | 机型L3（废弃） | varchar | 50 |  | √ | ' ' | 机型L3（废弃） |
| 45 | fprovidpart | 提供旧零件 | bpchar | 1 |  | √ | '0' | 提供旧零件 |
| 46 | fspraypartdownno | 底漆件号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 47 | fheatmaterialno | 原材料编号（热处理） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 48 | fspraypartdown | 底漆 | bpchar | 1 |  | √ | '0' | 底漆 |
| 49 | frawmaterialno | 原材料编号（废弃） | varchar | 50 |  | √ | ' ' | 原材料编号（废弃） |
| 50 | fcertifier | 确认者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 51 | fcomparedoc | 参考文件 | varchar | 50 |  | √ | ' ' | 参考文件 |
| 52 | fapply | 申请者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 53 | fannauncement |  | varchar | 255 |  | √ | ' ' |  |
| 54 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 55 | fspraypartdownname1 | fspraypartdownname1 | varchar | 50 |  | √ | ' ' |  |
| 56 | fspraypartno | 零件号（零件喷漆） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 57 | fspraypartdowngrn | 底漆GRN | varchar | 50 |  | √ | ' ' | 底漆GRN |
| 58 | frecipient | 接收者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 59 | fworktype | 工作类型 | varchar | 50 |  | √ | ' ' | 工作类型,枚举: A :木作 |
| 60 | fbusinessstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: Z :暂存 A :已申请 B :已接收 C :已完成 D :已取回 E :已关闭 F :已取消 |
| 61 | frawmaterialtype | 原材料类型 | varchar | 50 |  | √ | ' ' | 原材料类型,枚举: A :Clad Sheet 包铝片 B :Bare Sheet 裸铝片 C :Extrusion 挤压型材 D :Plate 板材 E :Rivet 铆钉 F :Bar 条棒 G :Rod 圆棒 |
| 62 | fworkrequire | 工作要求 | varchar | 255 |  | √ | ' ' | 工作要求 |
| 63 | fworkplace | 工作地点 | varchar | 50 |  | √ | ' ' | 工作地点 |
| 64 | fpaintgrn | 油漆GRN | varchar | 50 |  | √ | ' ' | 油漆GRN |
| 65 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 66 | frequirefinalstatus_tag | 要求热处理到最终状态_详情 | text | 0 |  |  | null | 要求热处理到最终状态_详情 |
| 67 | fworkremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 68 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 69 | fjobnum | 检修工单号 | int8 | 64 |  | √ | 0 | 检修工单F7 pom_mroorderno_f7 |
| 70 | fheatgrn | GRN | varchar | 50 |  | √ | ' ' | GRN |
| 71 | fworkrequire_tag | 工作要求_详情 | text | 0 |  |  | null | 工作要求_详情 |
| 72 | fspraypartfaceno | 面漆件号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 73 | fpaintmaterial | 油漆件号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 74 | fspraypartfacegrn | 面漆GRN | varchar | 50 |  | √ | ' ' | 面漆GRN |
| 75 | fsurfacegrn | GRN | varchar | 50 |  | √ | ' ' | GRN |
| 76 | fworkenddate | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 77 | fannauncement_tag | 详情 | text | 0 |  |  | null | 详情 |
| 78 | ffinisher | 完成者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 79 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_coordinatione_fk |  | fbillno |
| 2 | pk_pom_coordination |  | fid |

---

## 关联子实体-子表 t_sfc_surface_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_surface_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_surface_lk_fk |  | fentryid |
| 2 | pk_sfc_surface_lk |  | fpkid |

---

## 跨行业协调单-分表 t_pom_coordination_w

- **表名称：** 跨行业协调单-分表
- **表名：** t_pom_coordination_w

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcardno | 工卡号 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 3 | fpreoutdate | 预计离场时间 | timestamp | 0 |  |  | null | 预计离场时间 |
| 4 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | fworkobject | 工作对象 | varchar | 255 |  | √ | ' ' | 工作对象 |
| 6 | flocation | 位置 | varchar | 255 |  | √ | ' ' | 位置 |
| 7 | fphonedesc | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 8 | fairmaterial | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 9 | fworkobject_tag | 工作对象_详情 | text | 0 |  |  | null | 工作对象_详情 |
| 10 | fworkreqdesc | 工作要求描述 | varchar | 255 |  | √ | ' ' | 工作要求描述 |
| 11 | flocation_tag | 位置_详情 | text | 0 |  |  | null | 位置_详情 |
| 12 | fworkreqdesc_tag | 工作要求描述_详情 | text | 0 |  |  | null | 工作要求描述_详情 |
| 13 | frecipientdept | 接收部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fapplydept | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pom_coordination_w |  | fphonedesc |
| 2 | pk_pom_coordination_w |  | fid |
