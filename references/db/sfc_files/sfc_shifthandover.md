# 班次工作交接(废弃)-sfc_shifthandover

## 项目-子表 t_sfc_shiftho_projentry

- **表名称：** 项目-子表
- **表名：** t_sfc_shiftho_projentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sfc_shiftho_projentry |  | fid,fseq |
| 2 | pk_t_sfc_shiftho_projentry |  | fentryid |

---

## 人员清单-多语言表 t_sfc_shiftho_persentry_l

- **表名称：** 人员清单-多语言表
- **表名：** t_sfc_shiftho_persentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_shiftho_persentry_l |  | fpkid |
| 2 | idx_t_sfc_shiftho_persentry_l |  | fentryid,flocaleid |

---

## 人员清单-子表 t_sfc_shiftho_persentry

- **表名称：** 人员清单-子表
- **表名：** t_sfc_shiftho_persentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcstimes | 班制时间 | varchar | 255 |  | √ | ' ' | 班制时间 |
| 4 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [班次 mpdm_workshifts](../mpdm_files/mpdm_workshifts.md) |
| 5 | fpersonid | 工号 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_manuperson](../mpdm_files/mpdm_manuperson.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcsid | 班制 | int8 | 64 |  | √ | 0 | [班制 mpdm_classsystem](../mpdm_files/mpdm_classsystem.md) |
| 9 | fcstimes_tag | 班制时间_详情 | text | 0 |  |  | '' | 班制时间_详情 |
| 10 | fshifttimes | 班次时间 | varchar | 255 |  | √ | ' ' | 班次时间 |
| 11 | fshifttimes_tag | 班次时间_详情 | text | 0 |  |  | '' | 班次时间_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_shiftho_persentry |  | fentryid |
| 2 | idx_t_sfc_shiftho_persentry |  | fid,fseq |

---

## 检修信息-子表 t_sfc_shiftho_ovhlentry

- **表名称：** 检修信息-子表
- **表名：** t_sfc_shiftho_ovhlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fisworklog | 是否有开工记录 | bpchar | 1 |  | √ | ' ' | 是否有开工记录 |
| 2 | fovhlordentryid | 检修工单计划分录F7 | int8 | 64 |  | √ | 0 | [检修工单分录F7(废弃) sfc_mroorder_f7](../sfc_files/sfc_mroorder_f7.md) |
| 3 | fisengrck | 工程师检查与否 | bpchar | 1 |  | √ | ' ' | 工程师检查与否 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fiscard | 是否有工卡 | bpchar | 1 |  | √ | ' ' | 是否有工卡 |
| 7 | fovhlbillno | 检修工单号 | varchar | 50 |  | √ | ' ' | 检修工单号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fissign | 是否有签卡 | bpchar | 1 |  | √ | ' ' | 是否有签卡 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_shiftho_ovhlentry |  | fdetailid |
| 2 | idx_t_sfc_shiftho_ovhlentry |  | fentryid,fseq |

---

## 班次工作交接(废弃)-主表 t_sfc_shiftho

- **表名称：** 班次工作交接(废弃)-主表
- **表名：** t_sfc_shiftho

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fhopersmobile | 交接人联系方式 | varchar | 50 |  | √ | ' ' | 交接人联系方式 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :完成反馈 |
| 5 | fhandoverpersonid | 交接人 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_manuperson](../mpdm_files/mpdm_manuperson.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fperscount | 总共人数 | int8 | 64 |  | √ | 1 | 总共人数 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | freceivedbyid | 接收人 | int8 | 64 |  | √ | 0 | [基础资料带组织模板 mpdm_manuperson](../mpdm_files/mpdm_manuperson.md) |
| 11 | fisspntcentryupd | 自动更新到常用库 | bpchar | 1 |  | √ | ' ' | 自动更新到常用库 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | findustryid | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 15 | fiscontentryupd | 注意事项自动更新到常用库 | bpchar | 1 |  | √ | ' ' | 注意事项自动更新到常用库 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fhandovertime | 交接日期 | timestamp | 0 |  |  | null | 交接日期 |
| 19 | fhandoverstatus | 交接状态 | varchar | 30 |  | √ | ' ' | 交接状态,枚举: A :接收 B :退回 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_shiftho |  | fid |
| 2 | idx_t_sfc_shiftho |  | fbillno,fcreatorid |

---

## 工作内容-子表 t_sfc_shiftho_contentry

- **表名称：** 工作内容-子表
- **表名：** t_sfc_shiftho_contentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisworklog | fisworklog | bpchar | 1 |  | √ | ' ' |  |
| 3 | fothfdbk | 其他反馈 | varchar | 255 |  | √ | ' ' | 其他反馈 |
| 4 | fdailyplanid | 关联日计划单据编号 | int8 | 64 |  | √ | 0 | 日计划(废弃) sfc_dailyplan |
| 5 | fisengrck | fisengrck | bpchar | 1 |  | √ | ' ' |  |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fiscard | fiscard | bpchar | 1 |  | √ | ' ' |  |
| 8 | fovhlordentryid | fovhlordentryid | int8 | 64 |  | √ | 0 |  |
| 9 | ftaskno | 关联任务编号 | varchar | 50 |  | √ | ' ' | 关联任务编号 |
| 10 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: A :未开工 B :开工 C :完工 |
| 11 | fcontent | 工作内容 | varchar | 255 |  | √ | ' ' | 工作内容 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fnotice | 注意事项 | varchar | 255 |  | √ | ' ' | 注意事项 |
| 14 | fissign | fissign | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_sfc_shiftho_contentry |  | fid,fseq |
| 2 | pk_t_sfc_shiftho_contentry |  | fentryid |

---

## 工作内容-多语言表 t_sfc_shiftho_contentry_l

- **表名称：** 工作内容-多语言表
- **表名：** t_sfc_shiftho_contentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fothfdbk | 其他反馈 | varchar | 255 |  | √ | ' ' | 其他反馈 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_shiftho_contentry_l |  | fpkid |
| 2 | idx_t_sfc_shiftho_contentry_l |  | fentryid,flocaleid |

---

## 特别提醒-子表 t_sfc_shiftho_spntcentry

- **表名称：** 特别提醒-子表
- **表名：** t_sfc_shiftho_spntcentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: Z :注意事项 T :特别提醒 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_shiftho_spntcentry |  | fentryid |
| 2 | idx_t_sfc_shiftho_spntcentry |  | fid,fseq |
