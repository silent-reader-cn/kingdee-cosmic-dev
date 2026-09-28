# bastax 模块表清单

> 本模块共收录 **84** 张表定义，来自 `bastax_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category bastax
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bastax_addressterms` | 地址条件-主表 | 20 | [bastax_addressterms.md](./bastax_addressterms.md) |
| 2 | `t_bastax_addressterms_l` | 地址条件-多语言表 | 4 | [bastax_addressterms.md](./bastax_addressterms.md) |
| 3 | `t_bastax_addressterms_m` | 地址条件-使用范围位图表 | 2 | [bastax_addressterms.md](./bastax_addressterms.md) |
| 4 | `t_bastax_addressterms_u` | 地址条件-使用范围表 | 3 | [bastax_addressterms.md](./bastax_addressterms.md) |
| 5 | `t_bastax_addresstype` | 地址类型-主表 | 9 | [bastax_addresstype.md](./bastax_addresstype.md) |
| 6 | `t_bastax_addresstype_l` | 地址类型-多语言表 | 4 | [bastax_addresstype.md](./bastax_addresstype.md) |
| 7 | `t_bastax_bill_interface` | 单据接口注册-主表 | 35 | [bastax_bill_interface.md](./bastax_bill_interface.md) |
| 8 | `t_bastax_bill_interface_l` | 单据接口注册-多语言表 | 4 | [bastax_bill_interface.md](./bastax_bill_interface.md) |
| 9 | `t_bastax_biztypecode` | 业务类型代码-主表 | 12 | [bastax_biztypecode.md](./bastax_biztypecode.md) |
| 10 | `t_bastax_biztypecode_l` | 业务类型代码-多语言表 | 4 | [bastax_biztypecode.md](./bastax_biztypecode.md) |
| 11 | `t_bastax_building` | 楼栋信息-主表 | 20 | [bastax_building.md](./bastax_building.md) |
| 12 | `t_bastax_building_l` | 楼栋信息-多语言表 | 4 | [bastax_building.md](./bastax_building.md) |
| 13 | `t_bastax_building_u` | 楼栋信息-使用范围表 | 3 | [bastax_building.md](./bastax_building.md) |
| 14 | `t_bastax_code_detailstype` | 税码明细结果类型-主表 | 11 | [bastax_code_detailstype.md](./bastax_code_detailstype.md) |
| 15 | `t_bastax_code_detailstype_l` | 税码明细结果类型-多语言表 | 4 | [bastax_code_detailstype.md](./bastax_code_detailstype.md) |
| 16 | `t_bastax_drccountry` | DRC国家或地区-主表 | 12 | [bastax_drccountry.md](./bastax_drccountry.md) |
| 17 | `t_bastax_drccountry_l` | DRC国家或地区-多语言表 | 4 | [bastax_drccountry.md](./bastax_drccountry.md) |
| 18 | `t_bastax_euproduct` | DRC特定产品-主表 | 14 | [bastax_euproduct.md](./bastax_euproduct.md) |
| 19 | `t_bastax_euproduct_l` | DRC特定产品-多语言表 | 4 | [bastax_euproduct.md](./bastax_euproduct.md) |
| 20 | `t_bastax_euproductbase` | 单据体-子表 | 8 | [bastax_euproduct.md](./bastax_euproduct.md) |
| 21 | `t_bastax_hscode` | 海关商品编码-主表 | 16 | [bastax_hscode.md](./bastax_hscode.md) |
| 22 | `t_bastax_hscode_l` | 海关商品编码-多语言表 | 4 | [bastax_hscode.md](./bastax_hscode.md) |
| 23 | `t_bastax_org_view` | 税务管控视图默认方案-主表 | 9 | [tctb_org_default_view.md](./tctb_org_default_view.md) |
| 24 | `t_bastax_org_view` | 税务管控视图-主表 | 9 | [tctb_org_view.md](./tctb_org_view.md) |
| 25 | `t_bastax_org_view` | 税务管控视图定制方案-主表 | 9 | [tctb_org_view_custom.md](./tctb_org_view_custom.md) |
| 26 | `t_bastax_party` | 交易方资质-主表 | 21 | [bastax_party.md](./bastax_party.md) |
| 27 | `t_bastax_party_l` | 交易方资质-多语言表 | 4 | [bastax_party.md](./bastax_party.md) |
| 28 | `t_bastax_party_m` | 交易方资质-使用范围位图表 | 2 | [bastax_party.md](./bastax_party.md) |
| 29 | `t_bastax_party_type` | 交易方资质类型-主表 | 9 | [bastax_party_type.md](./bastax_party_type.md) |
| 30 | `t_bastax_party_type_l` | 交易方资质类型-多语言表 | 4 | [bastax_party_type.md](./bastax_party_type.md) |
| 31 | `t_bastax_party_u` | 交易方资质-使用范围表 | 3 | [bastax_party.md](./bastax_party.md) |
| 32 | `t_bastax_process` | 自定义税要素-主表 | 21 | [bastax_process.md](./bastax_process.md) |
| 33 | `t_bastax_process_l` | 自定义税要素-多语言表 | 4 | [bastax_process.md](./bastax_process.md) |
| 34 | `t_bastax_process_m` | 自定义税要素-使用范围位图表 | 2 | [bastax_process.md](./bastax_process.md) |
| 35 | `t_bastax_process_type` | 自定义税要素类型-主表 | 12 | [bastax_process_type.md](./bastax_process_type.md) |
| 36 | `t_bastax_process_type_l` | 自定义税要素类型-多语言表 | 4 | [bastax_process_type.md](./bastax_process_type.md) |
| 37 | `t_bastax_process_u` | 自定义税要素-使用范围表 | 3 | [bastax_process.md](./bastax_process.md) |
| 38 | `t_bastax_room` | 房间基础信息-主表 | 24 | [bastax_room.md](./bastax_room.md) |
| 39 | `t_bastax_room_l` | 房间基础信息-多语言表 | 6 | [bastax_room.md](./bastax_room.md) |
| 40 | `t_bastax_saleformat` | 销售业态-主表 | 10 | [bastax_saleformat.md](./bastax_saleformat.md) |
| 41 | `t_bastax_saleformat_l` | 销售业态-多语言表 | 4 | [bastax_saleformat.md](./bastax_saleformat.md) |
| 42 | `t_bastax_stage` | 分期信息-主表 | 19 | [bastax_stage.md](./bastax_stage.md) |
| 43 | `t_bastax_stage_l` | 分期信息-多语言表 | 4 | [bastax_stage.md](./bastax_stage.md) |
| 44 | `t_bastax_stage_u` | 分期信息-使用范围表 | 3 | [bastax_stage.md](./bastax_stage.md) |
| 45 | `t_bastax_supervision` | 监管方式-主表 | 12 | [bastax_supervision.md](./bastax_supervision.md) |
| 46 | `t_bastax_supervision_l` | 监管方式-多语言表 | 5 | [bastax_supervision.md](./bastax_supervision.md) |
| 47 | `t_bastax_taxarea` | 税收辖区-主表 | 14 | [bastax_taxarea.md](./bastax_taxarea.md) |
| 48 | `t_bastax_taxarea_l` | 税收辖区-多语言表 | 3 | [bastax_taxarea.md](./bastax_taxarea.md) |
| 49 | `t_bastax_taxcode` | 税码-主表 | 30 | [bastax_taxcode.md](./bastax_taxcode.md) |
| 50 | `t_bastax_taxcode_details` | 税码明细-子表 | 10 | [bastax_taxcode.md](./bastax_taxcode.md) |
| 51 | `t_bastax_taxcode_l` | 税码-多语言表 | 4 | [bastax_taxcode.md](./bastax_taxcode.md) |
| 52 | `t_bastax_taxcode_m` | 税码-使用范围位图表 | 2 | [bastax_taxcode.md](./bastax_taxcode.md) |
| 53 | `t_bastax_taxcode_taxrate` | 税率表-子表 | 4 | [bastax_taxcode.md](./bastax_taxcode.md) |
| 54 | `t_bastax_taxcode_type` | 税码分类-主表 | 19 | [bastax_taxcode_type.md](./bastax_taxcode_type.md) |
| 55 | `t_bastax_taxcode_type_l` | 税码分类-多语言表 | 4 | [bastax_taxcode_type.md](./bastax_taxcode_type.md) |
| 56 | `t_bastax_taxcode_type_m` | 税码分类-使用范围位图表 | 2 | [bastax_taxcode_type.md](./bastax_taxcode_type.md) |
| 57 | `t_bastax_taxcode_type_u` | 税码分类-使用范围表 | 3 | [bastax_taxcode_type.md](./bastax_taxcode_type.md) |
| 58 | `t_bastax_taxcode_u` | 税码-使用范围表 | 3 | [bastax_taxcode.md](./bastax_taxcode.md) |
| 59 | `t_bastax_taxgroup` | 税组-主表 | 22 | [bastax_taxgroup.md](./bastax_taxgroup.md) |
| 60 | `t_bastax_taxgroup_entry` | 单据体-子表 | 5 | [bastax_taxgroup.md](./bastax_taxgroup.md) |
| 61 | `t_bastax_taxgroup_l` | 税组-多语言表 | 4 | [bastax_taxgroup.md](./bastax_taxgroup.md) |
| 62 | `t_bastax_taxgroup_m` | 税组-使用范围位图表 | 2 | [bastax_taxgroup.md](./bastax_taxgroup.md) |
| 63 | `t_bastax_taxgroup_u` | 税组-使用范围表 | 3 | [bastax_taxgroup.md](./bastax_taxgroup.md) |
| 64 | `t_bastax_taxorg` | 税务组织信息-主表 | 14 | [bastax_taxorg.md](./bastax_taxorg.md) |
| 65 | `t_bastax_taxorg_applytax` | 适用税种-多选基础资料表 | 3 | [bastax_taxorg.md](./bastax_taxorg.md) |
| 66 | `t_bastax_taxorg_applytax` | 适用税种-多选基础资料表 | 3 | [bastax_taxorg_entry.md](./bastax_taxorg_entry.md) |
| 67 | `t_bastax_taxorg_area` | 税收辖区-多选基础资料表 | 3 | [bastax_taxorg.md](./bastax_taxorg.md) |
| 68 | `t_bastax_taxorg_area` | 税收辖区-多选基础资料表 | 3 | [bastax_taxorg_entry.md](./bastax_taxorg_entry.md) |
| 69 | `t_bastax_taxorg_entity` | 单据体-子表 | 9 | [bastax_taxorg.md](./bastax_taxorg.md) |
| 70 | `t_bastax_taxorg_entity` | 税务组织信息分录-主表 | 9 | [bastax_taxorg_entry.md](./bastax_taxorg_entry.md) |
| 71 | `t_bastax_taxorgan` | 税务机关-主表 | 15 | [bastax_taxorgan.md](./bastax_taxorgan.md) |
| 72 | `t_bastax_taxorgan_l` | 税务机关-多语言表 | 5 | [bastax_taxorgan.md](./bastax_taxorgan.md) |
| 73 | `t_bastax_taxproduct` | 税务产品-主表 | 24 | [bastax_taxproduct.md](./bastax_taxproduct.md) |
| 74 | `t_bastax_taxproduct_l` | 税务产品-多语言表 | 5 | [bastax_taxproduct.md](./bastax_taxproduct.md) |
| 75 | `t_bastax_taxproduct_m` | 税务产品-使用范围位图表 | 2 | [bastax_taxproduct.md](./bastax_taxproduct.md) |
| 76 | `t_bastax_taxproduct_u` | 税务产品-使用范围表 | 3 | [bastax_taxproduct.md](./bastax_taxproduct.md) |
| 77 | `t_bastax_taxproject` | 税务项目信息-主表 | 22 | [bastax_taxproject.md](./bastax_taxproject.md) |
| 78 | `t_bastax_taxproject_l` | 税务项目信息-多语言表 | 4 | [bastax_taxproject.md](./bastax_taxproject.md) |
| 79 | `t_bastax_taxprojectgroup` | 税务项目类别-主表 | 10 | [bastax_taxprojectgroup.md](./bastax_taxprojectgroup.md) |
| 80 | `t_bastax_taxprojectgroup_l` | 税务项目类别-多语言表 | 4 | [bastax_taxprojectgroup.md](./bastax_taxprojectgroup.md) |
| 81 | `t_bastax_taxprojectsds` | 所得税-子表 | 6 | [bastax_taxproject.md](./bastax_taxproject.md) |
| 82 | `t_bastax_taxprojectswyt` | 土地增值税-子表 | 7 | [bastax_taxproject.md](./bastax_taxproject.md) |
| 83 | `t_bastax_terms_detail` | 地址条件-子表 | 8 | [bastax_addressterms.md](./bastax_addressterms.md) |
| 84 | `t_tctb_org_view_detail` | 单据体-子表 | 7 | [tctb_org_view.md](./tctb_org_view.md) |
