# 输入输出要求-模板-plm_pm_delivercfg_tpl

## 要求状态-多选基础资料表 t_plm_pm_dctpl_reqstatus

- **表名称：** 要求状态-多选基础资料表
- **表名：** t_plm_pm_dctpl_reqstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [交付物状态配置 plm_pm_deliverable_status](../plmpm_files/plm_pm_deliverable_status.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_dctpl_reqstatus |  | fpkid |
| 2 | idx_plm_pm_dctpl_reqstatus_fk |  | fid |

---

## 输入输出要求-模板-主表 t_plm_pm_delivercfg_tpl

- **表名称：** 输入输出要求-模板-主表
- **表名：** t_plm_pm_delivercfg_tpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftemplateid | 模板ID | varchar | 50 |  | √ | ' ' | 模板ID |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcomments | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 7 | frelatedataid | 关联数据ID | int8 | 64 |  | √ | 0 | 关联数据ID |
| 8 | foutputfolder | 输出文件夹 | int8 | 64 |  | √ | 0 | [系统文件夹 plm_pdm_folder_hub](../plmsm_files/plm_pdm_folder_hub.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | frelatedatatype | 关联数据类型 | varchar | 50 |  | √ | ' ' | 关联数据类型,枚举: project :项目 taskgroup :任务组 task :任务 |
| 12 | fseqnumber | 顺序 | int8 | 64 |  | √ | 0 | 顺序 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcedelivercfg | 源配置 | int8 | 64 |  | √ | 0 | 源配置 |
| 15 | fismain | 是否主体 | int8 | 64 |  | √ | 0 | 是否主体 |
| 16 | fdeliverablemodel | 分类 | int8 | 64 |  | √ | 0 | [输入输出类型配置 plm_pm_deliverable_model](../plmpm_files/plm_pm_deliverable_model.md) |
| 17 | fproject | 项目 | int8 | 64 |  | √ | 0 | [项目模板 plm_pm_projecttpl](../plmpm_files/plm_pm_projecttpl.md) |
| 18 | fcount | 数量 | int8 | 64 |  | √ | 0 | 数量 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | finputfolder | 输入文件夹 | int8 | 64 |  | √ | 0 | [系统文件夹 plm_pdm_folder_hub](../plmsm_files/plm_pdm_folder_hub.md) |
| 22 | ftemplate | 模板 | varchar | 200 |  | √ | ' ' | 模板 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_delivercfg_tpl_m0 |  | fbillno |
| 2 | pk_plm_pm_delivercfg_tpl |  | fid |

---

## 输入来源-多选基础资料表 t_plm_pm_dctpl_source

- **表名称：** 输入来源-多选基础资料表
- **表名：** t_plm_pm_dctpl_source

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [任务模板 plm_pm_tasktpl](../plmpm_files/plm_pm_tasktpl.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_dctpl_source |  | fpkid |
| 2 | idx_plm_pm_dctpl_source_fk |  | fid |
